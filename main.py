from mcp.server.fastmcp import FastMCP
from typing import Optional, List

import tools.planetterp as planetterp
import tools.umdio as umdio
from tools.common import ApiOutput

mcp = FastMCP("umd-courses")


@mcp.tool()
async def get_a_course_wrapper(name: str, reviews: Optional[bool] = False) -> ApiOutput:
    return await planetterp.get_a_course(name, reviews)


@mcp.tool()
async def get_courses_wrapper(
    department: str,
    reviews: Optional[bool] = False,
    limit: Optional[int] = 100,
    offset: Optional[int] = 0,
) -> ApiOutput:
    return await planetterp.get_courses(department, reviews, limit, offset)


@mcp.tool()
async def get_a_professor_wrapper(
    name: str, reviews: Optional[bool] = False
) -> ApiOutput:
    return await planetterp.get_a_professor(name, reviews)


@mcp.tool()
async def get_all_professors_wrapper(
    type: str,
    reviews: bool = False,
    limit: Optional[int] = 100,
    offset: Optional[int] = 0,
) -> ApiOutput:
    return await planetterp.get_all_professors(type, reviews, limit, offset)


@mcp.tool()
async def get_grades(
    course: str, professor: str, semester: str, section: str
) -> ApiOutput:
    return await planetterp.get_grades(course, professor, semester, section)


@mcp.tool()
async def list_of_courses_wrapper(
    sort: Optional[str],
    page: Optional[int],
    per_page: Optional[int],
    semester: Optional[str],
    credits: Optional[str],
    dept_id: Optional[str],
    gen_ed: Optional[str],
) -> ApiOutput:
    return await umdio.list_of_courses(
        sort, page, per_page, semester, credits, dept_id, gen_ed
    )


@mcp.tool()
async def list_of_minified_courses_wrapper(
    sort: str, page: int, per_page: int, semester: str
) -> ApiOutput:
    return await umdio.list_of_minified_courses(sort, page, per_page, semester)


@mcp.tool()
async def list_of_sections_wrapper(
    sort: str,
    page: int,
    per_page: int,
    course_id: str,
    seats: str,
    open_seats: str,
    waitlist: str,
    semester: str,
) -> ApiOutput:
    return await umdio.list_of_sections(
        sort, page, per_page, course_id, seats, open_seats, waitlist, semester
    )


@mcp.tool()
async def view_specific_sections_wrapper(
    section_ids: List[str], semester: str
) -> ApiOutput:
    return await umdio.view_specific_sections(section_ids, semester)


@mcp.tool()
async def view_specific_courses_wrapper(
    course_ids: List[str], semester: str
) -> ApiOutput:
    return await umdio.view_specific_courses(course_ids, semester)


@mcp.tool()
async def view_sections_for_a_course_wrapper(
    course_ids: List[str], semester: str
) -> ApiOutput:
    return await umdio.view_sections_for_a_course(course_ids, semester)


@mcp.tool()
async def view_specific_sections_for_a_course_wrapper(
    course_ids: List[str], section_ids: List[str], semester: str
) -> ApiOutput:
    return await umdio.view_specific_sections_for_a_course(
        course_ids, section_ids, semester
    )


@mcp.tool()
async def list_semesters_wrapper() -> ApiOutput:
    return await umdio.list_semesters()


@mcp.tool()
async def list_departments_wrapper() -> ApiOutput:
    return await umdio.list_departments()


@mcp.tool()
async def list_professors_wrapper(name: str, course_id: str) -> ApiOutput:
    return await umdio.list_professors(name, course_id)


@mcp.tool()
async def list_majors_wrapper() -> ApiOutput:
    return await umdio.list_majors()


if __name__ == "__main__":
    mcp.run(transport="stdio")
