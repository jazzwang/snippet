<#setting number_format="computer">
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<?xml-stylesheet type="text/xsl" href="CDA.xsl"?>
<ClinicalDocument xmlns="urn:hl7-org:v3" xmlns:cda="urn:hl7-org:v3" xmlns:sdtc="urn:hl7-org:sdtc" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <!-- ** CDA Header ** -->
    <!-- US Realm Header (V3) -->
    <realmCode code="US"/>
    <typeId root="2.16.840.1.113883.1.3" extension="POCD_HD000040"/>
    <templateId root="2.16.840.1.113883.10.20.22.1.1" extension="2015-08-01"/>
    <!-- Procedure Note (V3) -->
    <templateId root="2.16.840.1.113883.10.20.22.1.6" extension="2015-08-01"/>
    <id root="2.16.840.1.113883.19.5.99999.1" extension="${id}"/>
    <code code="28570-0" displayName="Procedure Note" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC"/>
    <title>Procedure Note: ${name}</title>
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
    <!-- CDA Body -->
    <component>
        <structuredBody>
            <!-- Complications Section (V3) -->
            <#include "complications.ftl" parse=false>
            <!-- Procedure Description Section -->
            <#include "procedure_description.ftl" parse=false>
            <!-- Procedure Indications Section (V2) -->
            <#include "procedure_indications.ftl" parse=false>
            <!-- Postoperative Diagnosis Section (V3) -->
            <#include "postoperative_diagnosis_v3.ftl" parse=false>
        </structuredBody>
    </component>
</ClinicalDocument>