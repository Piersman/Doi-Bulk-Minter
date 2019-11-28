xmltemplate = """<?xml version="1.0" encoding="UTF-8"?>
<resource xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://datacite.org/schema/kernel-4" xsi:schemaLocation="http://datacite.org/schema/kernel-4 http://schema.datacite.org/meta/kernel-4.3/metadata.xsd">
  <identifier identifierType="DOI">doiIDENTIFIER</identifier>
  <creators>
    <creator>
      <creatorName>doiCREATOR</creatorName>
    </creator>
  </creators>
  <titles>
    <title xml:lang="en">doiTITLE</title>
  </titles>
  <publisher xml:lang="en">doiPUBLISHER</publisher>
  <publicationYear>doiTIME_COVERAGE</publicationYear>
  <subjects>
    <subject xml:lang="en">doiSUBJECT</subject>
  </subjects>
  <language>doiLANGUAGE</language>
  <resource TyperesourceTypeGeneral="Dataset">doiTYPE</resourceType>
  <sizes>
    <size>doiNUMBER_OF_RECORDS</size>
  </sizes>
  <formats>
    <format>doiFORMAT</format>
  </formats>
  <rightsList>
    <rights xml:lang="en-US">doiRIGHTS</rights></rightsList>
  <descriptions>
    <description xml:lang="en" descriptionType="Abstract">doiDESCRIPTION</description>
  </descriptions>
  <geoLocations>
    <geoLocation>
      <geoLocationPlace>doiGEOGRAPHICAL_COVERAGE</geoLocationPlace>
    </geoLocation>
  </geoLocations>
</resource>
"""