from tools.common import ApiOutput, make_http_call
from typing import Optional

PLANET_TERP_API_BASE_URL = "https://planetterp.com/api/v1"


async def get_a_course(name: str, reviews: Optional[bool] = False) -> ApiOutput:
    return await make_http_call(
        url=f"{PLANET_TERP_API_BASE_URL}/course",
        params={"name": name, "reviews": reviews},
    )


async def get_courses(
    department: str,
    reviews: Optional[bool] = False,
    limit: Optional[int] = 100,
    offset: Optional[int] = 0,
) -> ApiOutput:
    return await make_http_call(
        url=f"{PLANET_TERP_API_BASE_URL}/courses",
        params={
            "department": department,
            "reviews": reviews,
            "limit": limit,
            "offset": offset,
        },
    )


async def get_a_professor(name: str, reviews: Optional[bool] = False) -> ApiOutput:
    return await make_http_call(
        url=f"{PLANET_TERP_API_BASE_URL}/professor",
        params={"name": name, "reviews": reviews},
    )


async def get_all_professors(
    type: str,
    reviews: bool = False,
    limit: Optional[int] = 100,
    offset: Optional[int] = 0,
) -> ApiOutput:
    return await make_http_call(
        url=f"{PLANET_TERP_API_BASE_URL}/professors",
        params={"type": type, "reviews": reviews, "limit": limit, "offset": offset},
    )


async def get_grades(
    course: str, professor: str, semester: str, section: str
) -> ApiOutput:
    return await make_http_call(
        url=f"{PLANET_TERP_API_BASE_URL}/grades",
        params={
            "course": course,
            "professor": professor,
            "semester": semester,
            "section": section,
        },
    )
