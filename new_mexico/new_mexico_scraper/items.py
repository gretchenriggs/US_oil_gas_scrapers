# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class WellDetailsItem(Item):
    """Container for scraped data from the New Mexico Website"""
    well_id = Field()
    api_number = Field()
    well_no = Field()
    property_name = Field()
    property_number = Field()
    operator_number = Field()
    operator_name = Field()
    status =  Field()
    well_type =  Field()
    work_type =  Field()
    direction =  Field()
    multi_lateral =  Field()
    mineral_owner =  Field()
    surface_owner =  Field()
    surface_location =  Field()
    latitude =  Field()
    longitude =  Field()
    coord_sys =  Field()
    gl_elevation =  Field()
    kb_elevation =  Field()
    df_elevation =  Field()
    sing_mult_completion =  Field()
    potash_waiver =  Field()
    prop_form =  Field()
    prop_depth =  Field()
    tvd =  Field()
    mvd =  Field()
    pbd =  Field()
    init_apd_apprv =  Field()
    apd_eff =  Field()
    apd_exp =  Field()
    apd_cancel =  Field()
    apd_ext =  Field()
    spud =  Field()
    ta_date =  Field()
    ta_exp =  Field()
    shut_in =  Field()
    pa_intent =  Field()
    pa_date =  Field()
    site_release =  Field()
    last_insp =  Field()
    gas_cap_plan =  Field()
    ta_exp =  Field()
    pnr_exp =  Field()
    last_mit_bht =  Field()

    pass
