import scrapy
# from colorado_scraper.models import find_between_r, replace_blanks_clean
# from colorado_scraper.items import WellDetailsItem
# from scrapy.loader import ItemLoader
# from scrapy.loader.processors import Join, MapCompose
# from sqlalchemy import Date, Integer, cast
# import datetime
# import logging

class WellDetailsSpider(scrapy.Spider):
    name = "CO_well_details"

    scrapy.utils.log.configure_logging(install_root_handler=False)
    logging.basicConfig(
            filename='log.txt',
            format='%(levelname)s: %(message)s',
            level=logging.INFO
            )

    def start_requests(self):
        urls = ['http://cogcc.state.co.us/cogis/FacilityDetail.asp?facid=00108115&type=WELL']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]    # response parm is instance
        filename = 'quotes-%s.html' % page    #     of TextResponse that holds
        with open(filename, 'wb') as f:       #     page contatent
            f.write(response.body)            # Extracts scraped data as dicts
        self.log('Saved file %s' % filename)  #     & finds new URLs to follow

        # main = {find_between_r(span_id,'main_lbl','">'): find_between_r(span_id,'">','</span>') for span_id in response.xpath('//span[@id]').extract()}
        # gen_info = {find_between_r(span_id,'GeneralWellInformation_lbl','">'): find_between_r(span_id,'">','</span>') for span_id in response.xpath('//span[@id]').extract()}
        # replace_blanks_clean(gen_info)
        # gen_info_loc = {find_between_r(span_id,'GeneralWellInformation_Location_lbl','">'): find_between_r(span_id,'">','</span>') for span_id in response.xpath('//span[@id]').extract()}
        # replace_blanks_clean(gen_info_loc)
        # op_info = {find_between_r(span_id,'Operator_lbl','">'): find_between_r(span_id,'">','</span>') for span_id in response.xpath('//span[@id]').extract()}
        # replace_blanks_clean(op_info)
        #
        # il = ItemLoader(item=WellDetailsItem())
        # il.default_input_processor = MapCompose(unicode.strip)
        # il.default_output_processor = Join()
        # il.add_value('well_id', main['Api" title="API, Property Name and Well Number'][2:12].replace('-','').lstrip("0"))
        # il.add_value('api_number', main['Api" title="API, Property Name and Well Number'][0:12])
        # il.add_value('well_no', main['Api" title="API, Property Name and Well Number'].split("#")[1])
        # il.add_value('property_name', main['Api" title="API, Property Name and Well Number'][12:].split("#")[0])
        # il.add_value('property_number', find_between_r(main['PropertyId" title="Property Id'], '[',']'))
        # il.add_value('operator_name', op_info['OperatorName" title="Operator Name'])
        # il.add_value('operator_number', find_between_r(op_info['Ogrid" title="Ogrid'],'[',']'))
        # il.add_value('status', gen_info['Status'])
        # il.add_value('well_type', gen_info['WellType'])
        # il.add_value('work_type', gen_info['WorkType'])
        # il.add_value('direction', gen_info['DirectionalStatus'])
        # il.add_value('multi_lateral', gen_info['MultiLateral'])
        # il.add_value('mineral_owner', gen_info['MineralOwner'])
        # il.add_value('surface_owner', gen_info['SurfaceOwner'])
        # il.add_value('surface_location', gen_info_loc['Location" title="Location'])
        # il.add_value('latitude', gen_info_loc['Coordinates'].split(',')[0])
        # il.add_value('longitude', gen_info_loc['Coordinates'].split(',')[1].split(' ')[0])
        # il.add_value('coord_sys', gen_info_loc['Coordinates'].split(',')[1].split(' ')[1])
        # il.add_value('gl_elevation', gen_info['GLElevation'])
        # il.add_value('kb_elevation', gen_info['KBElevation'])
        # il.add_value('df_elevation', gen_info['DFElevation'])
        # il.add_value('sing_mult_completion', gen_info['Completions'])
        # il.add_value('potash_waiver', gen_info['PotashWaiver'])
        # il.add_value('prop_form', gen_info['ProposedFormation" class="full" style="min-height: 30px; display: block;'])
        # il.add_value('prop_depth', gen_info['ProposedDepth'])
        # il.add_value('tvd', gen_info['MeasuredDepth'])
        # il.add_value('mvd', gen_info['MeasuredVerticalDepth'])
        # il.add_value('pbd', gen_info['PlugbackMeasuredDpth'])
        # il.add_value('init_apd_apprv', gen_info['ApdInitialApprovalDate'])
        # il.add_value('apd_eff', gen_info['ApdEffectiveDate'])
        # il.add_value('apd_exp', gen_info['ApdExpirationDate'])
        # il.add_value('apd_cancel', gen_info['ApdCancellationDate'])
        # il.add_value('apd_ext', gen_info['ApdExtensionApprovalEffectiveDate'])
        # il.add_value('spud', gen_info['SpudDate'])
        # il.add_value('ta_date', gen_info['TADate'])
        # il.add_value('ta_exp', gen_info['TAExpirationDate'])
        # il.add_value('shut_in', gen_info['ShutInWaitingForPipelineDate'])
        # il.add_value('pa_intent', gen_info['PluggedAbandonedDateIntent'])
        # il.add_value('pa_date', gen_info['PluggedDate'])
        # il.add_value('site_release', gen_info['SiteReleaseDate'])
        # il.add_value('last_insp', gen_info['LastInspectionDate'])
        # il.add_value('gas_cap_plan', gen_info['GasCapturePlanDate'])
        # il.add_value('pnr_exp', gen_info['PluggedNotReleasedExpirationDate'])
        # il.add_value('last_mit_bht', gen_info['LastMitDate'])


        # return il.load_item()
