import inspect
import json

import pytest

from arcor2.cached import CachedProject, CachedScene
from arcor2.data.common import Action, ActionParameter, ActionPoint, Position, Project, Scene, SceneObject
from arcor2.data.object_type import ParameterMeta
from arcor2.exceptions import Arcor2Exception
from arcor2.object_types.abstract import Generic
from arcor2.parameter_plugins import ParameterPluginException
from arcor2.parameter_plugins.integer import IntegerParameterExtra, IntegerPlugin
from arcor2.parameter_plugins.utils import plugin_from_instance, plugin_from_type
from arcor2.source.utils import find_function, parse_def


class TestObject(Generic):
    def action(self, arbitrary_type_param: str, int_param: int, some_other_param: int) -> None:

        assert 0 <= int_param <= 10


param_name = "int_param"


def test_abstract() -> None:
    assert not inspect.isabstract(IntegerPlugin)


def test_plugin_from_type() -> None:

    assert plugin_from_type(int) is IntegerPlugin


def test_meta() -> None:

    meta = ParameterMeta(param_name, IntegerPlugin.type_name())
    IntegerPlugin.meta(meta, TestObject.action, find_function(TestObject.action.__name__, parse_def(TestObject)))
    assert meta.extra

    extra = IntegerParameterExtra.from_json(meta.extra)

    assert extra.minimum == 0
    assert extra.maximum == 10


@pytest.mark.parametrize(
    "val",
    [0, 1, 10],
)
class TestParametrized:
    def test_plugin_from_instance(self, val: float) -> None:

        assert plugin_from_instance(val) is IntegerPlugin

    def test_value_to_json(self, val: float) -> None:

        assert IntegerPlugin.value_to_json(val) == json.dumps(val)

    def test_get_value(self, val: float) -> None:

        scene = Scene("s1")
        obj = SceneObject("test_name", TestObject.__name__)
        scene.objects.append(obj)
        project = Project("p1", "s1")
        ap1 = ActionPoint("ap1", Position())
        project.action_points.append(ap1)

        invalid_param_name = "invalid_param"

        ac1 = Action(
            "ac1",
            f"{obj.id}/{TestObject.action.__name__}",
            parameters=[
                ActionParameter(param_name, IntegerPlugin.type_name(), IntegerPlugin.value_to_json(val)),
                ActionParameter(invalid_param_name, IntegerPlugin.type_name(), json.dumps("non_sense")),
            ],
        )

        ap1.actions.append(ac1)

        cscene = CachedScene(scene)
        cproject = CachedProject(project)

        with pytest.raises(Arcor2Exception):
            IntegerPlugin.parameter_value({}, cscene, cproject, ac1.id, "non_sense")

        with pytest.raises(Arcor2Exception):
            IntegerPlugin.parameter_value({}, cscene, cproject, "non_sense", param_name)

        with pytest.raises(ParameterPluginException):
            IntegerPlugin.parameter_value({}, cscene, cproject, ac1.id, invalid_param_name)

        value = IntegerPlugin.parameter_value({}, cscene, cproject, ac1.id, param_name)
        exe_value = IntegerPlugin.parameter_execution_value({}, cscene, cproject, ac1.id, param_name)

        assert value == val
        assert value == exe_value
