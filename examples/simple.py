import falcon

from typing import List, Dict

from ceeder import TagAnnotator


def txt_to_cdr_tags(_) -> List:
    entity_dict = {}
    entity_dict["offset_start"] = 0
    entity_dict["offset_end"] = 1
    entity_dict["tag"] = "LOC"
    return ([entity_dict], falcon.HTTP_200)


def create_tag():
    tag_anno = TagAnnotator(txt_to_cdr_tags, label="simple analytic",)
    return tag_anno.create()
