from mcp.server.fastmcp import FastMCP
from typing import Optional, List

import tools.planetterp as planetterp
import tools.umdio as umdio
from tools.common import ApiOutput

mcp = FastMCP("umd-courses")


@mcp.tool()
async def get_a_course_wrapper(name: str, reviews: Optional[bool] = False) -> ApiOutput:
    """
    Get details about a course

    Inputs:
    - name (str, required): e.g., MATH410
    - reviews (bool, optional): True to include student reviews, defaults to False
    """
    return await planetterp.get_a_course(name, reviews)


@mcp.tool()
async def get_courses_wrapper(
    department: str,
    reviews: Optional[bool] = False,
    limit: Optional[int] = 100,
    offset: Optional[int] = 0,
) -> ApiOutput:
    """
    Get all courses, in alphabetical order

    Inputs:
    - department (str, optional): e.g., MATH. Must be four characters. Defaults to all departments
    - reviews (bool, optional): True to include student reviews, defaults to False
    - limit (int, optional): Maximum number of records to return, defaults to 100, must be in range 1 to 100
    - offset (int, optional): Number of records to skip for pagination, defaults to 0, must be non negative
    """
    return await planetterp.get_courses(department, reviews, limit, offset)


@mcp.tool()
async def get_a_professor_wrapper(
    name: str, reviews: Optional[bool] = False
) -> ApiOutput:
    """
    Get the specified professor.

    slug is PlanetTerp's identifier for professors. Slugs are unique to a professor and is often, but not always, their last name.

    You may find a professor's slug useful to get a unique identifier for professors, or to link to a professor's page on PlanetTerp (via https://planetterp.com/professor/SLUG).

    For example, Jon Snow's slug might be snow.

    Inputs:
    - name (str, required): e.g., Jon Snow, usually has to be the full name of the professor, call get_all_professors tool for clues if need be
    - reviews (bool, optional): True to include student reviews, defaults to False
    """
    return await planetterp.get_a_professor(name, reviews)


@mcp.tool()
async def get_all_professors_wrapper(
    type: str,
    reviews: bool = False,
    limit: Optional[int] = 100,
    offset: Optional[int] = 0,
) -> ApiOutput:
    """
    Get all professors, in alphabetical order

    May be useful if you do not know the full name of a professor and need some clues

    Inputs:
    - type (str, optional): one of either "ta" (aka teaching assistant) or "professor", defaults to showing both
    - reviews (bool, optional): True to include student reviews, defaults to False
    - limit (int, optional): Maximum number of records to return, defaults to 100, must be in range 1 to 100
    - offset (int, optional): Number of records to skip for pagination, defaults to 0, must be non negative
    """
    return await planetterp.get_all_professors(type, reviews, limit, offset)


@mcp.tool()
async def get_grades(
    course: str, professor: str, semester: str, section: str
) -> ApiOutput:
    """
    Get grades for a course, a professor, or both. If by course, returns all of the grades available by section.

    At least one of course and professor is required.

    Inputs:
    - course (str, optional): e.g., MATH410
    - professor (str, optional): e.g., Jon Snow, usually has to be the full name of the professor, call list_professors tool for clues if need be, or call get_a_course if you know the course they teach as well
    - semester (str, optional): Show only grades for the given semester. Semester should be provided as the year followed by the semester code. 01 means Spring and 08 means Fall. For example, 202001 means Spring 2020. Default: all semesters
    - section (str, optional): e.g., 0101
    """
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
    """
    Returns paginated list of courses

    Inputs:
    - sort (str, optional): A comma-separated list of course properties. Defaults to ASCENDING order, use a - (minus) prefix for DESCENDING order. For example, ?sort=course_id,-credits sorts the results ASCENDING by course_id and DESCENDING by credits. Example: course_id,-credits
    - page (int, optional): For paginated responses, the page to view. 1-indexed. Defaults to 1 if omitted. Example: 3
    - per_page (int, optional): Endpoints that return a large amount of items are paginated to 30 items by default. You can use this parameter to set a page size up to 100. Example: 3
    - semester (str, optional): 6-digit semester ID to search, with optional comparator, separated by a pipe. Valid comparators are eq, leq, lt, gt, geq, neq. Example: 202008|leq
    - credits (str, optional): The number of credits to watch, with optional comparator, separated by a pipe. Valid comparators are eq, leq, lt, gt, geq, neq. Example: 3|leq
    - dept_id (str, optional): 4 Letter department code to search. Example: CMSC
    - gen_ed (str, optional): Gened requirement to search. Example: DSNS
    """
    return await umdio.list_of_courses(
        sort, page, per_page, semester, credits, dept_id, gen_ed
    )


@mcp.tool()
async def list_of_minified_courses_wrapper(
    sort: str, page: int, per_page: int, semester: str
) -> ApiOutput:
    """
    Returns list of all course codes and names

    Inputs:
    - sort (str, optional): A comma-separated list of course properties. Defaults to ASCENDING order, use a - (minus) prefix for DESCENDING order. For example, ?sort=course_id,-credits sorts the results ASCENDING by course_id and DESCENDING by credits. Example: course_id,-credits
    - page (int, optional): For paginated responses, the page to view. 1-indexed. Defaults to 1 if omitted. Example: 3
    - per_page (int, optional): Endpoints that return a large amount of items are paginated to 30 items by default. You can use this parameter to set a page size up to 100. Example: 3
    - semester (str, optional): 6-digit semester ID to search, with optional comparator, separated by a pipe. Valid comparators are eq, leq, lt, gt, geq, neq. Example: 202008|leq
    """
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
    """
    Returns paginated list of sections

    Inputs:
    - sort (str, optional): A comma-separated list of course properties. Defaults to ASCENDING order, use a - (minus) prefix for DESCENDING order. For example, ?sort=course_id,-credits sorts the results ASCENDING by course_id and DESCENDING by credits. Example: course_id,-credits
    - page (int, optional): For paginated responses, the page to view. 1-indexed. Defaults to 1 if omitted. Example: 3
    - per_page (int, optional): Endpoints that return a large amount of items are paginated to 30 items by default. You can use this parameter to set a page size up to 100. Example: 3
    - course_id (str, optional): 7 or 8 digit course id. See the course object for more info. Example: CMSC216
    - seats (str, optional): Number of total seats in a section, with optional comparator, separated by a pipe. Valid comparators are eq, leq, lt, gt, geq, neq. Example: 200
    - open_seats (str, optional): Number of open seats in a section, with optional comparator, separated by a pipe. Valid comparators are eq, leq, lt, gt, geq, neq. Example: 5
    - waitlist (str, optional): Number of people on the waitlist for a class, with optional comparator, separated by a pipe. Valid comparators are eq, leq, lt, gt, geq, neq. Example: 10
    - semester (str, optional): 6-digit semester ID to search, with optional comparator, separated by a pipe. Valid comparators are eq, leq, lt, gt, geq, neq. Example: 202008|leq
    """
    return await umdio.list_of_sections(
        sort, page, per_page, course_id, seats, open_seats, waitlist, semester
    )


@mcp.tool()
async def view_specific_sections_wrapper(
    section_ids: List[str], semester: str
) -> ApiOutput:
    """
    Returns paginated list of specific sections

    Inputs:
    - section_ids (list[str], required): One or more section ids, of format DEPTNNN-XXXX.
    - semester (str, optional): 6-digit semester ID to search, with optional comparator, separated by a pipe. Valid comparators are eq, leq, lt, gt, geq, neq. Example: 202008|leq
    """
    return await umdio.view_specific_sections(section_ids, semester)


@mcp.tool()
async def view_specific_courses_wrapper(
    course_ids: List[str], semester: str
) -> ApiOutput:
    """
    Returns info about one or more courses

    Inputs:
    - course_ids (list[str], required): One or more course ids, of format DEPTNNN with up to 2 trailing characters.
    - semester (str, optional): 6-digit semester ID to search, with optional comparator, separated by a pipe. Valid comparators are eq, leq, lt, gt, geq, neq. Example: 202008|leq
    """
    return await umdio.view_specific_courses(course_ids, semester)


@mcp.tool()
async def view_sections_for_a_course_wrapper(
    course_ids: List[str], semester: str
) -> ApiOutput:
    """
    Returns section info about one or more courses

    Inputs:
    - course_ids (list[str], required): One or more course ids, of format DEPTNNN with up to 2 trailing characters.
    - semester (str, optional): 6-digit semester ID to search, with optional comparator, separated by a pipe. Valid comparators are eq, leq, lt, gt, geq, neq. Example: 202008|leq
    """
    return await umdio.view_sections_for_a_course(course_ids, semester)


@mcp.tool()
async def view_specific_sections_for_a_course_wrapper(
    course_ids: List[str], section_ids: List[str], semester: str
) -> ApiOutput:
    """
    Returns specific section info about one or more courses

    Inputs:
    - course_ids (list[str], required): One or more course ids, of format DEPTNNN with up to 2 trailing characters.
    - section_ids (list[str], required): One or more section ids, of format DEPTNNN-XXXX.
    - semester (str, optional): 6-digit semester ID to search, with optional comparator, separated by a pipe. Valid comparators are eq, leq, lt, gt, geq, neq. Example: 202008|leq
    """
    return await umdio.view_specific_sections_for_a_course(
        course_ids, section_ids, semester
    )


@mcp.tool()
async def list_semesters_wrapper() -> ApiOutput:
    """
    Returns list of all available semesters, each in format YYYYMM. Might be useful if you don't know specific ones.
    """
    return await umdio.list_semesters()


@mcp.tool()
async def list_departments_wrapper() -> ApiOutput:
    """
    Returns list of all available departments. Might be useful if you don't know specific ones.
    """
    return await umdio.list_departments()


@mcp.tool()
async def list_professors_wrapper(name: str, course_id: str) -> ApiOutput:
    """
    Returns list of all professors

    Inputs:
    - name (str, optional): Professor's name (almost always full name). Example: Aaron Bartlett
    - course_id (str, optional): 7 or 8 digit course id. See the course object for more info. Example: CMSC216
    """
    return await umdio.list_professors(name, course_id)


@mcp.tool()
async def list_majors_wrapper() -> ApiOutput:
    """
    Get a list of all majors
    """
    return await umdio.list_majors()


if __name__ == "__main__":
    mcp.run(transport="stdio")
