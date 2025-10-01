import pytest
import reflex as rx

from portfolio.admin import (basics_editor,
                              basics_view,
                              work_editor,
                              work_view,
                              education_editor,
                              education_view,
                              projects_editor,
                              projects_view,
                              sidebar_navigation,
                              main_content,
                              admin_page)


class TestBasicsComponents:
    """Test basics editor and view components."""

    def test_basics_editor_renders(self):
        """Test that basics editor component renders."""
        component = basics_editor()

        assert isinstance(component, rx.Component)

    def test_basics_view_renders(self):
        """Test that basics view component renders."""
        component = basics_view()

        assert isinstance(component, rx.Component)


class TestWorkComponents:
    """Test work editor and view components."""

    def test_work_editor_renders(self):
        """Test that work editor component renders."""
        component = work_editor()

        assert isinstance(component, rx.Component)

    def test_work_view_renders(self):
        """Test that work view component renders."""
        component = work_view()

        assert isinstance(component, rx.Component)


class TestEducationComponents:
    """Test education editor and view components."""

    def test_education_editor_renders(self):
        """Test that education editor component renders."""
        component = education_editor()

        assert isinstance(component, rx.Component)

    def test_education_view_renders(self):
        """Test that education view component renders."""
        component = education_view()

        assert isinstance(component, rx.Component)


class TestProjectsComponents:
    """Test projects editor and view components."""

    def test_projects_editor_renders(self):
        """Test that projects editor component renders."""
        component = projects_editor()

        assert isinstance(component, rx.Component)

    def test_projects_view_renders(self):
        """Test that projects view component renders."""
        component = projects_view()

        assert isinstance(component, rx.Component)


class TestSidebarNavigation:
    """Test sidebar navigation component."""

    def test_sidebar_navigation_renders(self):
        """Test that sidebar navigation renders."""
        component = sidebar_navigation()

        assert isinstance(component, rx.Component)


class TestMainContent:
    """Test main content area component."""

    def test_main_content_renders(self):
        """Test that main content area renders."""
        component = main_content()

        assert isinstance(component, rx.Component)


class TestAdminPage:
    """Test admin page main component."""

    def test_admin_page_renders(self):
        """Test that admin page renders."""
        component = admin_page()

        assert isinstance(component, rx.Component)
