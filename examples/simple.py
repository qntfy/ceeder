import falcon

from typing import List, Dict

from seeder import TagAnnotator, FacetAnnotator


def txt_to_cdr_tags(_) -> List:
    entity_dict = {}
    entity_dict['offset_start'] = 0
    entity_dict['offset_end'] = 1
    entity_dict['tag'] = 'LOC'
    return [entity_dict]


def create_tag():
    tag_anno = TagAnnotator(txt_to_cdr_tags,
                            label='simple analytic',
    )
    return tag_anno.create()


def create_facet():
    fx = lambda x: [{'value': "hello", 'confidence': 0.99}]
    anno = FacetAnnotator(fx,
                          label='facet analytic',
    )
    return anno.create()
