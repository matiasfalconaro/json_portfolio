# CHANGELOG

## Versioning System
This project follows Semantic Versioning x.y.z:
- MAJOR version (x): Breaking changes, major functionality shifts, and
  significant refactoring.
- MINOR version (y): New features, important improvements, and substantial
  enhancements.
- PATCH version (z): Bug fixes, minor improvements, documentation updates,
  and hot-fixes.

### Version Format
[x.y.z] - yyyy-mm-dd - [ENVIRONMENT/TYPE] - [LIFE-CICLE]
(x = 0): BC, POC, MVP,
(x > 0): RC, GA, MTT, LTS, EOL, CANARY

Where:
- `x.y.z`: Semantic version number (MAJOR.MINOR.PATCH)
- `yyyy-mm-dd`: Date when the version was released
- `[LIFE-CICLE]`: Deployment context or deliverable type:
[BC]:Bussines-Concept
[POC]:Prove-of-concept
[MVP]: Minimum-viable-product
[RC]: Release-candidate
[GA]: General-availability
[MTT]: Maintenance
[LTS]: Long-term-support
[EOL]: End-of-life
[CANARY]: Canary
- `[ENVIRONMENT/TYPE]`:
[GH]: Ready-to-DEV
[DEV]: Development
[QAS]: Testing
[STG]: Staging
[UAT]: User-aceptance-testing
[PRD]: Productivd
[STP]: Stopped

## Branching
1. Create the issue named after the version
   #X "vx.y.z"
2. Create the branch named after the version
   `git branch vx.y.z`
3. Open a PR named after the version and issue
   `vx.y.z #X`
4. Commits during development
5. Squash with rebase before merging
   (commits) ──► "vx.y.z"
6. Update changelog
7. Pull Request of version
8. Merge into main
9. Tag in Git
   "vx.y.z"
10. Push tag to GitHub

```
Issue ──► Branch ──► Commits ──► Squash ──► Changelog  ──► PR      ──►      Merge ──► Tag
#X        vx.y.z                                           vx.y.z #X #Y
vx.y.z    vx.y.z                 vx.y.z                    vx.y.z           vx.y.z
```

## Change Types
- `Added`: New features, endpoints, models, or functionality
- `Changed`: Modifications to existing functionality
- `Deprecated`: Features that will be removed in future releases
- `Removed`: Features that have been deleted
- `Fixed`: Bug fixes and error corrections
- `Security`: Vulnerability patches and security improvements

## ######################################################################

## [POC] 2025-2-3 [v0.0.0] - [GH]
### Added
- Layout wireframing
- Json resume

## [POC] 2025-10-3 [v0.1.0] - [GH]
### Added
- Contact and source code odals
- Picture
- Icons standarization
- Resume downloading feature

### Changed
- Modularization
- States management
- Styling modularization

## [MVP] 2025-13-3 [v1.1.0] - [GH]
### Changed
- Changed font size in `link_style`.
- Removed ENV API_URL=https://mfalconaro.onrender.com.
- Reformatted CMD to multi-line for readability.
- Changed "summary" in `resume.json`.
- Changed display text instead of a GitHub link when the repository is under "NDA".
- Changed role in project "Investment app".
- Update `resume.pdf`.

### Added
- Port asignation in `Dockerfile`
- Added PEP8 to`rxconfig.py`
- Added latest projects to `resume.json`.

### Fixed
- Improved "projects" section identation in `resume.json`

## [MVP] 2025-9-2 [v1.2.0] - [DEV]
### Changed
- Remove certificates.

### Fixed
- Project cards responsivess and theme compatibility.
- Navbar, footer and modals theme compatibility.


## [MVP] 2025-9-2 [v1.3.0] - [GH]
### Added
- Implement CI/CD pipeline using `Git Actions` and `DockerHub`.

### Changed
- Update PDF resume to v1.3.0

### Fixed
- Github and LinkedIn links were broken.

## [MVP] 2025-9-2 [v1.3.1] - [DEV]
### Changed
- Modify CI/CD worflow

## [MVP] 2025-9-13 [v1.3.2] - [DEV]
### Added
- `README.md`.

### Changed
- `Reflex-EC2-toolkit` card stack.

## [MVP] 2025-9-13 [v1.3.3] - [DEV]
### Hotfix
- Update version in source code modal

## [MVP] 2025-9-3 [v1.3.4] - [DEV]
### Added
- Update `CHANGELOG.md`
- Update `README.md`

### Changed
- email in `resume.json`
- Update version in frontend

## [MVP] 2025-9-13 [v1.3.5] - [DEV]
### Changed
- implement `version.txt` to simplify versioning in the frontend.

### Fix
- implement `find_resume_pdf()` to keep versioning my resumes in their names.
- Change `header_section()` to integrate the new function.

## [MVP] 2025-9-13 [v1.3.6] - [GH]
### Fix
- Fix `find_resume_pdf()`

### Changed
- implement `version.txt`

### Notes
This version is not included in the [Dockerhub repository](https://hub.docker.com/repository/docker/mlfalconaro/portfolio-reflex/general) because it failed while building its image.

## [MVP] 2025-9-13 [v1.3.7] - [DEV]
### Changed
- Update `Dockerfile`

### Changed
- implement `version.txt`

## [MVP] 2025-9-13 [v1.3.8] - [DEV]
### Rollback
- `header_section()` is rolled back to `v1.3.4` of the feature `Resume Download Button`.

### Changed
- implement `version.txt`

## [MVP] 2025-9-13 [v1.3.9] - [DEV]
### Fixed
- `resume.pdf` from A0 to A4

## [MVP] 2025-9-13 [v1.3.10] - [DEV]
### Fixed
- Typos.


## [MVP] 2025-9-19 [v1.4.0] - [DEV]
### Added
- Unit tests for all components, data, links, assets, portfolio, states, and utils.
- Test coverage verification for images, PDFs, and external URLs.

### Changed
- Updated `version.txt` to reflect v1.4.0.

### Fixed
- Paths in asset tests corrected.
- Resume file path corrected for testing.
- Footer text comparison fixed to properly decode.

## [MVP] 2025-9-19 [v1.4.1] - [DEV]
### Changed
- Updated `version.txt` to reflect v1.4.1.
- Update unit tests
- Add `README.md` to the docker image

### Fixed
- Add type hints and docstrings to remaining methods

## [MVP] 2025-9-20 [v1.4.2] - [DEV]
### Added
- BDD Testing Framework: Implemented Behavior-Driven Development testing using pytest-bdd
- Gherkin Feature Files: Added .feature files for all test scenarios in tests/features/
- Step Definitions: Created step implementation files in tests/steps/ for all BDD tests
- Comprehensive BDD Coverage: 16 BDD scenarios across 6 test categories

### Changed
README Documentation: Updated testing section to include BDD commands and test structure

#Notes
- Backward Compatibility: All existing unit tests maintained and continue to pass
- Mixed Approach: Both unit testing and BDD testing coexist, providing comprehensive test coverage

## [MVP] 2025-09-21 [v1.5.0] - [GH]
### Added
- Implement MongoDB as a Dockerized microservice for portfolio data.
- Bulk import of existing `resume.json` data into MongoDB collections.
- Docker Compose configuration to orchestrate Reflex app and MongoDB.
- GitHub Actions workflow extended to build and push multi-service setup.
- Initial test integration using `pytest` and `pytest-bdd`.

### Changed
- Replaced `JSON` file storage with MongoDB as the primary data source.
- Updated data access in Reflex components to fetch from MongoDB instead of `resume.json`.
- Generalized database configuration using environment variables.

### Fixed
- Added `pytest-bdd` to requirements.
- Ensured MongoDB collections are initialized with required indexes at startup.

### Notes
- MongoDB service runs in Docker with authentication (`admin/secret` by default).
- Reflex app now depends on the MongoDB service being available at startup.
- Tests can run either in CI (with Docker services) or locally with `docker-compose`.

## [MVP] 2025-09-22 [v1.5.1] - [GH]
### Fixed
- update GitHub Actions workflow to run tests using `docker compose exec`.

### Notes
- This release is a **workflow test only**; no functional changes were made to the application.

## [MVP] 2025-09-22 [v1.5.2] - [GH]
### Changed
- Refactored GitHub Actions workflow into separate `build`, `test`, and `push` jobs.
- `push` to DockerHub now only occurs if tests pass.
- Improved CI clarity and job dependency flow to prevent pushing failing builds.

## [MVP] 2025-09-22 [v1.5.3] - [DEV]
### Changed
- Update 'version format' in `CHANGELOG.md`.
- Refactored GitHub Actions workflow:
  - The same image tested in CI is used for push, avoiding unnecessary rebuilds.
- Updated `docker-compose.yml` to support two modes:
  - **Local development:** build the app from the Dockerfile (`BUILD_APP=.`).
  - **Production:** use the DockerHub image directly (`APP_IMAGE=<REGISTRY>/<NAMESPACE>/<APP>:<TAG>`), without rebuilding.
- MongoDB remains as the official image (`mongo:latest`) in both development and production.

## [MVP] 2025-09-22 [v2.0.0] - [GH]
### Added
- Admin CRUD Page.
- Add `admin/` styling to `styles.py`.
- Create layout for `admin/` elements.
- Frontend updates from MongoDB in real time.

### Changed
- Refactored state management: `AdminState` now handles collection-specific editing independently.
- Build command:
   - Removed `--env prod` to enable recompiling dinamically in each request (with manual refresh).
   - Update components from static, non-reactive call to a state.
- Update framework to `reflex==0.8.12`.
- Use absolute paths for section links.
- Improve self-documentation.

### Fixed
- Fixed missing typehints and docstrings.

> TODO
> - [1] Unit and BDD tests updated to cover new admin page and collection editing functionality.
> - [2] JWT authentication implemented for secure access to the admin panel.
> - [3] Update README: Simplify #testing - Update architecture diagram.
