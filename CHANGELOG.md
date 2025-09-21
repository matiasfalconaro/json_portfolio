# CHANGELOG

## Versioning System
This project follows Semantic Versioning 2.0.0:
- MAJOR version (x): Breaking changes, major functionality shifts, and
  significant refactoring
- MINOR version (y): New features, important improvements, and substantial
  enhancements
- PATCH version (z): Bug fixes, minor improvements, documentation updates,
  and hot-fixes

### Version Format
[x.y.z] - yyyy-mm-dd - [ENVIRONMENT/TYPE]

Where:
`x.y.z`: Semantic version number (MAJOR.MINOR.PATCH)
`yyyy-mm-dd`: Date when the version was released

`[ENVIRONMENT/TYPE]`: Deployment context or deliverable type:
[POC]: Proof-of-Concept
[MVP]: Minimum-Viable-Product
[DEV]: Development-environment
[QAS]: Quality-Assurance/Testing
[UAT]: User-Acceptance-Testing
[PRD]: Production-environment
[ALPHA]: Alpha-release
[BETA]: Beta-release
[RC]: Release-Candidate

## Branching
1. Crear un issue con el nombre de la versión
   #1 "vw.y.z"
2. Crear la rama con el nombre de la versión
   `git branch vx.y.z`
3. Commits durante el desarrollo
4. Squash con rebase antes del merge
   (commits) ──► "vx.y.z"
5. Actualizar el changelog
6. Pull Request de la versión
7. Merge a main
8. Tag en Git
   "vx.y.z"
9. Push del tag a GitHub

```
 Issue ──► Branch ──► Commits ──► Squash ──► Changelog ──► PR ──► Merge ──► Tag
 vx.y.z    vx.y.z                 vx.y.z                  vx.y.z            vx.y.z   
```

### Change Types
- `Added`: New features, endpoints, models, or functionality
- `Changed`: Modifications to existing functionality
- `Deprecated`: Features that will be removed in future releases
- `Removed`: Features that have been deleted
- `Fixed`: Bug fixes and error corrections
- `Security`: Vulnerability patches and security improvements

## ######################################################################

## 2025-2-3 [v0.0.0]
### Added
- Layout wireframing
- Json resume

## 2025-10-3 [v0.1.0]
### Added
- Contact and source code odals
- Picture
- Icons standarization
- Resume downloading feature

### Changed
- Modularization
- States management
- Styling modularization

## [MVP] 2025-13-3 [v1.1.0]
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

## [STG] 2025-9-2 [v1.2.0]
### Changed
- Remove certificates.

### Fixed
- Project cards responsivess and theme compatibility.
- Navbar, footer and modals theme compatibility.


## [DEV] 2025-9-2 [v1.3.0]
### Added
- Implement CI/CD pipeline using `Git Actions` and `DockerHub`.

### Changed
- Update PDF resume to v1.3.0

### Fixed
- Github and LinkedIn links were broken.

## [PRD] 2025-9-2 [v1.3.1]
### Changed
- Modify CI/CD worflow

## [PRD] 2025-9-13 [v1.3.2]
### Added
- `README.md`.

### Changed
- `Reflex-EC2-toolkit` card stack.

## [PRD] 2025-9-13 [v1.3.3]
### Hotfix
- Update version in source code modal

## [PRD] 2025-9-3 [v1.3.4]
### Added
- Update `CHANGELOG.md`
- Update `README.md`

### Changed
- email in `resume.json`
- Update version in frontend

## [PRD] 2025-9-13 [v1.3.5]
### Changed
- implement `version.txt` to simplify versioning in the frontend.

### Fix
- implement `find_resume_pdf()` to keep versioning my resumes in their names.
- Change `header_section()` to integrate the new function.

## [DEV] 2025-9-13 [v1.3.6]
### Fix
- Fix `find_resume_pdf()`

### Changed
- implement `version.txt`

### Notes
This version is not included in the [Dockerhub repository](https://hub.docker.com/repository/docker/mlfalconaro/portfolio-reflex/general) because it failed while building its image.

## [PRD] 2025-9-13 [v1.3.7]
### Changed
- Update `Dockerfile`

### Changed
- implement `version.txt`

## [PRD] 2025-9-13 [v1.3.8]
### Rollback
- `header_section()` is rolled back to `v1.3.4` of the feature `Resume Download Button`.

### Changed
- implement `version.txt`

## [PRD] 2025-9-13 [v1.3.9]
### Fixed
- `resume.pdf` from A0 to A4

## [PRD] 2025-9-13 [v1.3.10]
### Fixed
- Typos.


## [DEV] 2025-9-19 [v1.4.0]
### Added
- Unit tests for all components, data, links, assets, portfolio, states, and utils.
- Test coverage verification for images, PDFs, and external URLs.

### Changed
- Updated `version.txt` to reflect v1.4.0.

### Fixed
- Paths in asset tests corrected.
- Resume file path corrected for testing.
- Footer text comparison fixed to properly decode.

## [PRD] 2025-9-19 [v1.4.1]
### Changed
- Updated `version.txt` to reflect v1.4.1.
- Update unit tests
- Add `README.md` to the docker image

### Fixed
- Add type hints and docstrings to remaining methods

## [STG] 2025-9-20 [v1.4.2]
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
