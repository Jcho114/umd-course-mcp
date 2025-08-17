from typing import Optional, List
from tools.common import make_http_call, ApiOutput

UMD_IO_API_BASE_URL = "https://api.umd.io/v1"


async def list_of_courses(
    sort: Optional[str],
    page: Optional[int],
    per_page: Optional[int],
    semester: Optional[str],
    credits: Optional[str],
    dept_id: Optional[str],
    gen_ed: Optional[str],
) -> ApiOutput:
    return await make_http_call(
        url=f"{UMD_IO_API_BASE_URL}/courses",
        params={
            "sort": sort,
            "page": page,
            "per_page": per_page,
            "semester": semester,
            "credits": credits,
            "dept_id": dept_id,
            "gen_ed": gen_ed,
        },
    )


async def list_of_minified_courses(
    sort: str, page: int, per_page: int, semester: str
) -> ApiOutput:
    return await make_http_call(
        url=f"{UMD_IO_API_BASE_URL}/courses/list",
        params={
            "sort": sort,
            "page": page,
            "per_page": per_page,
            "semester": semester,
        },
    )


async def list_of_sections(
    sort: str,
    page: int,
    per_page: int,
    course_id: str,
    seats: str,
    open_seats: str,
    waitlist: str,
    semester: str,
) -> ApiOutput:
    return await make_http_call(
        url=f"{UMD_IO_API_BASE_URL}/courses/sections",
        params={
            "sort": sort,
            "page": page,
            "per_page": per_page,
            "course_id": course_id,
            "seats": seats,
            "open_seats": open_seats,
            "waitlist": waitlist,
            "semester": semester,
        },
    )


async def view_specific_sections(section_ids: List[str], semester: str) -> ApiOutput:
    return await make_http_call(
        url=f"{UMD_IO_API_BASE_URL}/courses/sections/{','.join(section_ids)}",
        params={"semester": semester},
    )


async def view_specific_courses(course_ids: List[str], semester: str) -> ApiOutput:
    return await make_http_call(
        url=f"{UMD_IO_API_BASE_URL}/courses/{','.join(course_ids)}",
        params={"semester": semester},
    )


async def view_sections_for_a_course(course_ids: List[str], semester: str) -> ApiOutput:
    return await make_http_call(
        url=f"{UMD_IO_API_BASE_URL}/courses/{','.join(course_ids)}/sections",
        params={"semester": semester},
    )


async def view_specific_sections_for_a_course(
    course_ids: List[str], section_ids: List[str], semester: str
) -> ApiOutput:
    return await make_http_call(
        url=f"{UMD_IO_API_BASE_URL}/courses/{','.join(course_ids)}/sections/{','.join(section_ids)}",
        params={"semester": semester},
    )


async def list_semesters() -> ApiOutput:
    return await make_http_call(url=f"{UMD_IO_API_BASE_URL}/courses/semesters")


async def list_departments() -> ApiOutput:
    return await make_http_call(url=f"{UMD_IO_API_BASE_URL}/courses/departments")


async def list_professors(name: str, course_id: str) -> ApiOutput:
    return await make_http_call(
        url=f"{UMD_IO_API_BASE_URL}/professors",
        params={"name": name, "course_id": course_id},
    )


async def list_majors() -> ApiOutput:
    return await make_http_call(url=f"{UMD_IO_API_BASE_URL}/majors/list")
