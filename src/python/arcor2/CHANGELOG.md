# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),


## [0.8.0] - WIP
### Changed
- Reorganisation of the repository - switched to monorepo based on [Pants](https://www.pantsbuild.org/docs/welcome-to-pants). The code was divided into more packages (that can be separatelly relased) within one repository.
- Tests now run on GitHub instead of CircleCi.
- Unification of objects and services
  - There is ```Generic``` base class for objects without pose, ```GenericWithPose``` for objects with pose and ```Robot``` class that should be base class for every robot.
- Integration of scene service (0.2.0).
- @action decorator is now added automatically in the run-time.
- ```Orientation``` dataclass now performs quaternion normalization in ```__post_init__```.
- ```Robot``` base class now has ```_move_lock``` mutex to ensure that only one move-action is called at the time.

## [0.8.0rc2] - 2020-09-16

## [0.8.0rc1] - 2020-09-15

## [0.8.0b8] - 2020-08-21
### Fixed
- Some robot-related issues fixed

## [0.8.0b7] - 2020-08-12
### Changed
- Scene service client: 'upsert_collision' now has optional 'mesh_parameters': parameter.

## [0.8.0b6] - 2020-08-03
### Changed
- New logic representation
- Unification of objects and services
- Integration of scene service

## [0.7.1] - 2020-07-15
### Fixed
- Fix of broken python package arcor2 0.7.0

## [0.7.0] - 2020-07-15
### Changed

- ARServer: new RPC 'TemporaryPackage'
- ARServer: RPC ObjectTypesChangedEvent renamed to ChangedObjectTypesEvent, now contains changed ObjectTypes meta instead of just type names
- ARServer: ShowMainScreenEvent.
- Package name added to PackageInfoEvent
- ARServer now compares its API_VERSION with API_VERSION of the Execution.
- ARServer: ShowMainScreenEvent will now not contain 'highlight' when sent to a newly connected UI.
- AP can now have another AP as parent
- rest: OptionalData now may contain list of primitive type.
- Execution: PackageStateEvent now contains package_id
- Execution: added 'executed' to PackageMeta

## [0.6.0] - 2020-06-19
### Changed

- Build/Execution proxy: allow port change using env. var.
- ARServer: RenameScene RPC now checks if scene name is unique and 'dry_run' works.
- ARServer: ListScenes/ListProjects now contain 'modified'.
- ARServer: DeleteObjectType RPC added.
- @action decorator is now compatible with Windows.
- Service class now has 'cleanup' method which is called when scene is closed or when script ends. Call of 'cleanup' can be disabled by 'export ARCOR_CLEANUP_SERVICES=False' - this is particularly useful when running the script manually again and again.
- Cleanup method for ObjectTypes.

## [0.5.1] - 2020-06-04
### Fixed
- ignoring check of return parameters
- allowing list of strings as request body

## [0.5.0] - 2020-06-01
### Changed
- ARServer container need to setup new env variable using docker-compose -> ARCOR2_DATA_PATH=/root/data
- ListProjects RPC now gets projects in parallel.
- dry_run parameter for selected RPCs
- EEF pose/robot joints streaming
- OpenScene, OpenProject, SceneClosed, ProjectClosed events.
- Execution proxy: use persistent websocket connection.
- SceneCollisionsEvent merged into PackageInfoEvent
- ARServer: RPC to cancel action execution.
- Execution package now contains package.json with its metadata. Execution service now supports renaming of packages.

## [0.4.3] - 2020-05-22
### Changed
- added support for CORS

## [0.4.2] - 2020-04-27
### Fixed
- Fix of functions to transform relative poses to absolute and vice versa

## [0.4.1] - 2020-04-22
### Added
- New RPCs for getting robot joints and effector pose
- New RPC to get IDs of EE and suctions
- Added pivot enum for UpdateObjectPoseUsingRobot

### Fixed
- Fix of remove action RPC
- Another fixes


## [0.4.0] - 2020-04-17
### Changed
- Complete redesign of RPC for ARClients (AREditor atm)
- Documentation of execution and build API
- Support for project service 0.2.0
- New and updated events
- Enhanced error messages
- Create (global) session to enable reuse of connections.

## [0.3.0] - 2020-03-24
### Changed
- Renamed RobotJoints to ProjectRobotJoints and ModelTypeEnum to Model3dType
- Added new services for Time and Logic related actons
- Added boolean parameter plugin
- Description, returns and origins fields marked as optional
- New event - ActionResult
- Separated script enabling discovery through UDP broadcast
- Support for list params
- Services and Action objects are now marked as disabled when some problem occured and error message is passed to GUI (previously such services/objects were ignored)
- Services with no configuration are disabled

## [0.2.1] - 2020-02-28
### Fixed
- Added compatibility with Project service v 0.1.1
- Param values and defaults are strings now
- min, max stored in extra as JSON string

## [0.2.0] - 2020-02-20
### Changed
- ExecuteAction RPC.
- Uuid for action object/point/action.
- Execution proxy PUT method
- ActionPoint class in execution package
- Removed loop in main script, when hasLogic == false
- Parameter values not send in currentAction event
- ProjectState RESUMED removed
- Execution: print out script output if not JSON.
- Joint: rotation -> value


## [0.1.7] - 2019-12-24
### Fixed
- Build: disable caching

## [0.1.5] - 2019-12-22
### Fixed
- Parameter plugins

## [0.1.4] - 2019-12-18
### Fixed
- Parameter of type relative_pose now accepts json string as value

## [0.1.3] - 2019-12-18
### Fixed
- N/A

## [0.1.2] - 2019-12-17
### Fixed
- bump docker version

## [0.1.1] - 2019-12-17
### Fixed
- bump docker version

## [0.1.1] - 2019-12-12
### Fixed
- N/A

## [0.1.0] - 2019-12-12
### Changed
- Separation of services.