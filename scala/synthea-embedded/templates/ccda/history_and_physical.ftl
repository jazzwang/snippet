<#setting number_format="computer">
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<?xml-stylesheet type="text/xsl" href="CDA.xsl"?>
<ClinicalDocument xmlns="urn:hl7-org:v3" xmlns:cda="urn:hl7-org:v3" xmlns:sdtc="urn:hl7-org:sdtc" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <!-- ** CDA Header ** -->
  <!-- US Realm Header (V3) -->
  <realmCode code="US"/>
  <typeId root="2.16.840.1.113883.1.3" extension="POCD_HD000040"/>
  <templateId root="2.16.840.1.113883.10.20.22.1.1" extension="2015-08-01"/>
  <!-- History and Physical (V3) -->
  <templateId root="2.16.840.1.113883.10.20.22.1.3" extension="2015-08-01"/>
  <id root="2.16.840.1.113883.19.5" extension="${id}" assigningAuthorityName="https://github.com/synthetichealth/synthea"/>
  <code code="34117-2" displayName="History and Physical Note" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC"/>
  <title>C-CDA R2.1 - History &amp; Physical: ${name}</title>
  <effectiveTime value="${time?number_to_date?string["yyyyMMddHHmmss"]}"/>
  <confidentialityCode code="N" codeSystem="2.16.840.1.113883.5.25"/>
  <languageCode code="en-US"/>
  <recordTarget>
    <patientRole>
      <id root="2.16.840.1.113883.19.5" extension="${id}" assigningAuthorityName="https://github.com/synthetichealth/synthea"/>
      <!-- HP is "primary home" from codeSystem 2.16.840.1.113883.5.1119 -->
      <addr use="HP">
        <streetAddressLine>${address}</streetAddressLine>
        <city>${city}</city>
        <state>${state}</state>
        <#if zip?has_content>
        <postalCode>${zip}</postalCode>
        <#else>
        <postalCode nullFlavor="NI"/>
        </#if>
        <!-- US is "United States" from ISO 3166-1 Country Codes: 1.0.3166.1 -->
		<country>US</country>
      </addr>
      <#if telecom?has_content>
      <telecom use="HP" value="tel:${telecom}"/>
      <#else>
      <telecom nullFlavor="NI"/>
      </#if>
      <patient>
        <name>
          <given>${name?keep_before_last(" ")}</given>
          <family>${name?keep_after_last(" ")}</family>
        </name>
        <administrativeGenderCode code="${gender}" codeSystem="2.16.840.1.113883.5.1" codeSystemName="HL7 AdministrativeGender"/>
        <!-- Date of birth need only be precise to the day -->
        <birthTime value="${birthdate?number_to_date?string["yyyyMMddHHmmss"]}"/>
        <!-- CDC Race and Ethnicity code set contains the five minimum race and ethnicity
					categories defined by OMB Standards -->
        <raceCode code="${race_lookup[race]}" displayName="${race}" codeSystemName="CDC Race and Ethnicity" codeSystem="2.16.840.1.113883.6.238"/>
        <!-- The raceCode extension is only used if raceCode is valued -->
        <ethnicGroupCode code="${ethnicity_lookup[race]}" displayName="${ethnicity_display_lookup[race]}" codeSystemName="CDC Race and Ethnicity" codeSystem="2.16.840.1.113883.6.238"/>
        <languageCommunication>
          <languageCode code="en-US"/>
        </languageCommunication>
      </patient>
    </patientRole>
  </recordTarget>
  <author>
    <time value="${time?number_to_date?string["yyyyMMddHHmmss"]}"/>
    <assignedAuthor>
      <id nullFlavor="NA"/>
      <addr nullFlavor="NA"/>
      <telecom nullFlavor="NA"/>
      <assignedAuthoringDevice>
        <manufacturerModelName>https://github.com/synthetichealth/synthea</manufacturerModelName>
        <softwareName>https://github.com/synthetichealth/synthea</softwareName>
      </assignedAuthoringDevice>
      <representedOrganization>
        <id nullFlavor="NA"/>
        <name>${preferredProviderwellness.name?replace("&", "&amp;")}</name>
        <telecom nullFlavor="NA"/>
        <addr>
          <streetAddressLine>${preferredProviderwellness.address?replace("&", "&amp;")}</streetAddressLine>
          <city>${preferredProviderwellness.city}</city>
          <state>${preferredProviderwellness.state}</state>
          <postalCode>${preferredProviderwellness.zip}</postalCode>
        </addr>
      </representedOrganization>
    </assignedAuthor>
  </author>
  <custodian>
    <assignedCustodian>
      <representedCustodianOrganization>
        <id nullFlavor="NA"/>
        <name>${preferredProviderwellness.name?replace("&", "&amp;")}</name>
        <telecom nullFlavor="NA"/>
        <addr>
          <streetAddressLine>${preferredProviderwellness.address?replace("&", "&amp;")}</streetAddressLine>
          <city>${preferredProviderwellness.city}</city>
          <state>${preferredProviderwellness.state}</state>
          <postalCode>${preferredProviderwellness.zip}</postalCode>
        </addr>
      </representedCustodianOrganization>
    </assignedCustodian>
  </custodian>
  <componentOf>
    <encompassingEncounter>
        <id extension="9937012" root="2.16.840.1.113883.19"/>
        <effectiveTime value="${time?number_to_date?string["yyyyMMddHHmmss"]}"/>
    </encompassingEncounter>
  </componentOf>
  <!-- CDA Body -->
    <component>
        <structuredBody>
            <!-- ALLERGIES AND INTOLERANCES SECTION (ENTRIES REQUIRED) V2 -->
            <#if ehr_allergies?has_content>
              <#include "allergies.ftl">
            <#else>
              <#include "allergies_no_current.ftl" parse=false>
            </#if>
            <!-- Family History Section (V3) -->
            <#include "family_history.ftl" parse=false>
            <!-- General Status Section -->
            <#include "general_status.ftl" parse=false>
            <!-- Past Medical History (V3) -->
            <#include "past_medical_history.ftl" parse=false>
            <!-- Medications Section (entries optional) (V2) -->
            <#if ehr_medications?has_content>
              <#include "medications.ftl">
            <#else>
              <#include "medications_no_current.ftl" parse=false>
            </#if>
            <!--Physical Exam Section (V3) -->
            <#include "physical_exam.ftl" parse=false>
            <!-- Results Section (entries optional) (V3) -->
            <#if ehr_reports?has_content>
              <#include "results.ftl">
            <#else>
              <#include "results_no_current.ftl" parse=false>
            </#if>
            <!-- Review of Systems Section -->
            <#include "review_of_systems.ftl" parse=false>
            <!-- Vital Signs Section (entries optional) (V3) -->
            <#if ehr_observations?has_content>
              <#include "vital_signs.ftl">
            <#else>
              <#include "vital_signs_no_current.ftl" parse=false>
            </#if>
        </structuredBody>
    </component>
</ClinicalDocument>