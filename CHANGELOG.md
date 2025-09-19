# CHANGELOG

# 2025-2-3 [v0.0.0]
## Added
- Layout wireframing
- Json resume

# 2025-10-3 [v0.1.0]
## Added
- Contact and source code odals
- Picture
- Icons standarization
- Resume downloading feature

## Changed
- Modularization
- States management
- Styling modularization

# [MVP] 2025-13-3 [v1.1.0]
## Changed
- Changed font size in `link_style`.
- Removed ENV API_URL=https://mfalconaro.onrender.com.
- Reformatted CMD to multi-line for readability.
- Changed "summary" in `resume.json`.
- Changed display text instead of a GitHub link when the repository is under "NDA".
- Changed role in project "Investment app".
- Update `resume.pdf`.

## Added
- Port asignation in `Dockerfile`
- Added PEP8 to`rxconfig.py`
- Added latest projects to `resume.json`.

## Fixed
- Improved "projects" section identation in `resume.json`

# [STG] 2025-9-2 [v1.2.0]
## Changed
- Remove certificates.

## Fixed
- Project cards responsivess and theme compatibility.
- Navbar, footer and modals theme compatibility.


# [DEV] 2025-9-2 [v1.3.0]
## Added
- Implement CI/CD pipeline using `Git Actions` and `DockerHub`.

## Changed
- Update PDF resume to v1.3.0

## Fixed
- Github and LinkedIn links were broken.

# [PRD] 2025-9-2 [v1.3.1]
## Changed
- Modify CI/CD worflow

# [PRD] 2025-9-13 [v1.3.2]
## Added
- `README.md`.

## Changed
- `Reflex-EC2-toolkit` card stack.

# [PRD] 2025-9-13 [v1.3.3]
## Hotfix
- Update version in source code modal

# [PRD] 2025-9-3 [v1.3.4]
## Added
- Update `CHANGELOG.md`
- Update `README.md`

## Changed
- email in `resume.json`
- Update version in frontend

# [PRD] 2025-9-13 [v1.3.5]
## Changed
- implement `version.txt` to simplify versioning in the frontend.

## Fix
- implement `find_resume_pdf()` to keep versioning my resumes in their names.
- Change `header_section()` to integrate the new function.

# [PRD] 2025-9-13 [v1.3.6]
## Fix
- Fix `find_resume_pdf()`

## Changed
- implement `version.txt`

## Notes
This version is not included in the [Dockerhub repository](https://hub.docker.com/repository/docker/mlfalconaro/portfolio-reflex/general) because it failed while building its image.

# [PRD] 2025-9-13 [v1.3.7]
## Changed
- Update `Dockerfile`

## Changed
- implement `version.txt`

# [PRD] 2025-9-13 [v1.3.8]
## Rollback
- `header_section()` is rolled back to `v1.3.4` of the feature `Resume Download Button`.

## Changed
- implement `version.txt`

# [PRD] 2025-9-13 [v1.3.9]
## Fixed
- `resume.pdf` from A0 to A4

# [PRD] 2025-9-13 [v1.3.10]
## Fixed
- Typos.


# [PRD] 2025-9-19 [v1.4.0]
## Added
- Unit tests for all components.

## Changed
- Updated `version.txt` to reflect v1.4.0.
- `get_version()` now returns `"1.4.0"`.

## Fixed
- Makdown structure and typos in `CHANGELOG.md`
