/*
	Global JavaScripts for FOIA
*/


/*
	Global variables
*/


var agencies=new Array();
var agenciesAb=new Array();
var agenciesFile=new Array();


agencies[0]='All Agencies';
agencies[1]='Department of Agriculture';
agencies[2]='Department of Commerce';
agencies[3]='Department of Defense';
agencies[4]='Department of Education';
agencies[5]='Department of Energy';
agencies[6]='Department of Health and Human Services';
agencies[7]='Department of Homeland Security';
agencies[8]='Department of Housing and Urban Development';
agencies[9]='Department of the Interior';
agencies[10]='Department of Justice';
agencies[11]='Department of Labor';
agencies[12]='Department of State';
agencies[13]='Department of Transportation';
agencies[14]='Department of the Treasury';
agencies[15]='Department of Veterans Affairs';

//Federal Agencies
agencies[16]='Administrative Conference of the United States';
agencies[17]='U.S. Agency for International Development';
agencies[18]='American Battle Monuments Commission';
agencies[19]='National Railroad Passenger Corporation (Amtrak)';
agencies[20]='Armed Forces Retirement Home';
agencies[21]='Broadcasting Board of Governors';
agencies[22]='Central Intelligence Agency';
agencies[23]='Chemical Safety and Hazard Investigation Board';
agencies[24]='U.S. Commission on Civil Rights';
agencies[25]='Committee for Purchase from People Who Are Blind or &#8230;';
agencies[26]='Commodity Futures Trading Commission';
agencies[27]='Consumer Financial Protection Bureau';
agencies[28]='U.S. Consumer Product Safety Commission';
agencies[29]='Corporation for National and Community Service';
agencies[30]='Council of Inspectors General on Integrity and Efficiency';
agencies[31]='Court Services and Offender Supervision Agency';
agencies[32]='Defense Nuclear Facilities Safety Board';
agencies[33]='Environmental Protection Agency';
agencies[34]='Equal Employment Opportunity Commission';
agencies[35]='Council on Environmental Quality';
agencies[36]='Office of Management and Budget';
agencies[37]='Office of National Drug Control Policy';
agencies[38]='Office of Science and Technology Policy';
agencies[39]='Office of the United States Trade Representative';
agencies[40]='Export-Import Bank of the U.S.';
agencies[41]='Farm Credit Administration';
agencies[42]='Farm Credit System Insurance Corporation';
agencies[43]='Federal Communications Commission';
agencies[44]='Federal Deposit Insurance Corporation';
agencies[45]='Federal Election Commission';
agencies[46]='Federal Energy Regulatory Commission';
agencies[47]='Federal Financial Institutions Council';
agencies[48]='Federal Housing Finance Agency';
agencies[49]='Federal Labor Relations Authority';
agencies[50]='Federal Maritime Commission';
agencies[51]='Federal Mediation And Conciliation Service';
agencies[52]='Federal Mine Safety and Health Review Commission';
agencies[53]='Federal Open Market Committee';
agencies[54]='Board of Governors of the Federal Reserve System';
agencies[55]='Federal Retirement Thrift Investment Board';
agencies[56]='Federal Trade Commission';
agencies[57]='U.S. General Services Administration';
agencies[58]='Institute of Museum and Library Services';
agencies[59]='Inter-American Foundation';
agencies[60]='Legal Services Corporation';
agencies[61]='Merit Systems Protection Board';
agencies[62]='Millennium Challenge Corporation';
agencies[63]='National Aeronautics and Space Administration';
agencies[64]='National Archives and Records Administration';
agencies[65]='National Capital Planning Commission';
agencies[66]='National Credit Union Administration';
agencies[67]='National Endowment for the Arts';
agencies[68]='National Endowment for the Humanities';
agencies[69]='National Indian Gaming Commision';
agencies[70]='National Labor Relations Board';
agencies[71]='National Mediation Board';
agencies[72]='National Science Foundation';
agencies[73]='National Transportation Safety Board';
agencies[74]='U.S. Nuclear Regulatory Commission';
agencies[75]='Occupational Safety and Health Review Commission';
agencies[76]='Office of Government Ethics';
agencies[77]='Office of Navajo and Hopi Indian Relocation';
agencies[78]='Office of Personnel Management';
agencies[79]='Office of Special Counsel';
agencies[80]='Office of the Director of National Intelligence';
agencies[81]='Overseas Private Investment Corporation';
agencies[82]='Peace Corps';
agencies[83]='Pension Benefit Guaranty Corporation';
agencies[84]='Postal Regulatory Commission';
agencies[85]='Privacy and Civil Liberties Oversight Board';
agencies[86]='Recovery Accountability and Transparency Board';
agencies[87]='Railroad Retirement Board';
agencies[88]='U.S. Securities and Exchange Commission';
agencies[89]='Selective Service System';
agencies[90]='U.S. Small Business Administration';
agencies[91]='Social Security Administration';
agencies[92]='Special Inspector General for Afghanistan Reconstruction';
agencies[93]='Special Inspector General for Iraq Reconstruction';
agencies[94]='Surface Transportation Board';
agencies[95]='Tennessee Valley Authority';
agencies[96]='U.S. Access Board';
agencies[97]='U.S. African Development Foundation';
agencies[98]='U.S. Copyright Office';
agencies[99]='U.S. International Boundary and Water Commission';
agencies[100]='U.S. International Trade Commission';
agencies[101]='U.S. Postal Service';
agencies[102]='United States Trade and Development Agency';





//agencies[95]='Office of Federal Housing Enterprise Oversight';


//Abbreviation of agencies

agenciesAb[0]='ALL';
agenciesAb[1]='USDA';
agenciesAb[2]='DOC';
agenciesAb[3]='DoD';
agenciesAb[4]='ED';
agenciesAb[5]='DOE';
agenciesAb[6]='HHS';
agenciesAb[7]='DHS';
agenciesAb[8]='HUD';
agenciesAb[9]='DOI';
agenciesAb[10]='DOJ';
agenciesAb[11]='U.S. DOL';
agenciesAb[12]='State';
agenciesAb[13]='DOT';
agenciesAb[14]='Treasury';
agenciesAb[15]='VA';

//Federal agencies
agenciesAb[16]='ACUS';
agenciesAb[17]='USAID';
agenciesAb[18]='ABMC';
agenciesAb[19]='NRPC';
agenciesAb[20]='AFRH';
agenciesAb[21]='BBG';
agenciesAb[22]='CIA';
agenciesAb[23]='CSB';
agenciesAb[24]='USCCR';
//agenciesAb[25]='CFP/Committee';
agenciesAb[25]='CPPBSD';
agenciesAb[26]='CFTC';
agenciesAb[27]='CFPB';
agenciesAb[28]='U.S. CPSC';
agenciesAb[29]='CNCS';
agenciesAb[30]='CIGIE';
agenciesAb[31]='CSOSA';
agenciesAb[32]='DNFSB';
agenciesAb[33]='EPA';
agenciesAb[34]='EEOC';
agenciesAb[35]='CEQ';
agenciesAb[36]='OMB';
agenciesAb[37]='ONDCP';
agenciesAb[38]='OSTP';
agenciesAb[39]='USTR';
agenciesAb[40]='Ex-Im Bank';
agenciesAb[41]='FCA';
agenciesAb[42]='FCSIC';
agenciesAb[43]='FCC';
agenciesAb[44]='FDIC';
agenciesAb[45]='FEC';
agenciesAb[46]='FERC';
agenciesAb[47]='FFIEC';
agenciesAb[48]='FHFA';
agenciesAb[49]='FLRA';
agenciesAb[50]='FMC';
agenciesAb[51]='FMCS';
agenciesAb[52]='FMSHRC';
agenciesAb[53]='FOMC';
agenciesAb[54]='FRB';
agenciesAb[55]='FRTIB';
agenciesAb[56]='FTC';
agenciesAb[57]='GSA';
agenciesAb[58]='IMLS';
agenciesAb[59]='IAF';
agenciesAb[60]='LSC';
agenciesAb[61]='MSPB';
agenciesAb[62]='MCC';
agenciesAb[63]='NASA';
agenciesAb[64]='NARA';
agenciesAb[65]='NCPC';
agenciesAb[66]='NCUA';
agenciesAb[67]='NEA';
agenciesAb[68]='NEH';
agenciesAb[69]='NIGC';
agenciesAb[70]='NLRB';
agenciesAb[71]='NMB';
agenciesAb[72]='NSF';
agenciesAb[73]='NTSB';
agenciesAb[74]='USNRC';
agenciesAb[75]='OSHRC';
agenciesAb[76]='OGE';
agenciesAb[77]='ONHIR';
agenciesAb[78]='OPM';
agenciesAb[79]='OSC';
agenciesAb[80]='ODNI';
agenciesAb[81]='OPIC';
agenciesAb[82]='PC';
agenciesAb[83]='PBGC';
agenciesAb[84]='PRC';
agenciesAb[85]='PCLOB';
agenciesAb[86]='RATB';
agenciesAb[87]='US RRB';
agenciesAb[88]='SEC';
agenciesAb[89]='SSS';
agenciesAb[90]='SBA';
agenciesAb[91]='SSA';
agenciesAb[92]='SIGAR';
agenciesAb[93]='SIGIR';
agenciesAb[94]='STB';
agenciesAb[95]='TVA';
agenciesAb[96]='USAB';
agenciesAb[97]='US ADF';
agenciesAb[98]='CO';
agenciesAb[99]='USIBWC';
agenciesAb[100]='USITC';
agenciesAb[101]='USPS';
agenciesAb[102]='USTDA';






//agenciesAb[95]='OFHEO';


//Where to file of agencies

agenciesFile[0]='ALL';
agenciesFile[1]='USDA';
agenciesFile[2]='DOC';
agenciesFile[3]='DoD';
agenciesFile[4]='ED';
agenciesFile[5]='DOE';
agenciesFile[6]='HHS';
agenciesFile[7]='DHS';
agenciesFile[8]='HUD';
agenciesFile[9]='DOI';
agenciesFile[10]='DOJ';
agenciesFile[11]='U.S. DOL';
agenciesFile[12]='State';
agenciesFile[13]='DOT';
agenciesFile[14]='Treasury';
agenciesFile[15]='VA';

//Federal agencies
agenciesFile[16]='ACUS';
agenciesFile[17]='USAID';
agenciesFile[18]='ABMC';
agenciesFile[19]='NRPC';
agenciesFile[20]='AFRH';
agenciesFile[21]='BBG';
agenciesFile[22]='CIA';
agenciesFile[23]='CSB';
agenciesFile[24]='USCCR';
agenciesFile[25]='CPPBSD';
agenciesFile[26]='CFTC';
agenciesFile[27]='CFPB';
agenciesFile[28]='U.S. CPSC';
agenciesFile[29]='CNCS';
agenciesFile[30]='CIGIE';
agenciesFile[31]='CSOSA';
agenciesFile[32]='DNFSB';
agenciesFile[33]='EPA';
agenciesFile[34]='EEOC';
agenciesFile[35]='CEQ';
agenciesFile[36]='OMB';
agenciesFile[37]='ONDCP';
agenciesFile[38]='OSTP';
agenciesFile[39]='USTR';
agenciesFile[40]='Ex-Im Bank';
agenciesFile[41]='FCA';
agenciesFile[42]='FCSIC';
agenciesFile[43]='FCC';
agenciesFile[44]='FDIC';
agenciesFile[45]='FEC';
agenciesFile[46]='FERC';
agenciesFile[47]='FFIEC';
agenciesFile[48]='FHFA';
agenciesFile[49]='FLRA';
agenciesFile[50]='FMC';
agenciesFile[51]='FMCS';
agenciesFile[52]='FMSHRC';
agenciesFile[53]='FOMC';
agenciesFile[54]='FRB';
agenciesFile[55]='FRTIB';
agenciesFile[56]='FTC';
agenciesFile[57]='GSA';
agenciesFile[58]='IMLS';
agenciesFile[59]='IAF';
agenciesFile[60]='LSC';
agenciesFile[61]='MSPB';
agenciesFile[62]='MCC';
agenciesFile[63]='NASA';
agenciesFile[64]='NARA';
agenciesFile[65]='NCPC';
agenciesFile[66]='NCUA';
agenciesFile[67]='NEA';
agenciesFile[68]='NEH';
agenciesFile[69]='NIGC';
agenciesFile[70]='NLRB';
agenciesFile[71]='NMB';
agenciesFile[72]='NSF';
agenciesFile[73]='NTSB';
agenciesFile[74]='USNRC';
agenciesFile[75]='OSHRC';
agenciesFile[76]='OGE';
agenciesFile[77]='ONHIR';
agenciesFile[78]='OPM';
agenciesFile[79]='OSC';
agenciesFile[80]='ODNI';
agenciesFile[81]='OPIC';
agenciesFile[82]='PC';
agenciesFile[83]='PBGC';
agenciesFile[84]='PRC';
agenciesFile[85]='PCLOB';
agenciesFile[86]='RATB';
agenciesFile[87]='US RRB';
agenciesFile[88]='SEC';
agenciesFile[89]='SSS';
agenciesFile[90]='SBA';
agenciesFile[91]='SSA';
agenciesFile[92]='SIGAR';
agenciesFile[93]='SIGIR';
agenciesFile[94]='STB';
agenciesFile[95]='TVA';
agenciesFile[96]='USAB';
agenciesFile[97]='US ADF';
agenciesFile[98]='CO';
agenciesFile[99]='USIBWC';
agenciesFile[100]='USITC';
agenciesFile[101]='USPS';
agenciesFile[102]='USTDA';




//agenciesFile[94]='OFHEO';


var windowPopup="popupMsg";

function popupWinClose(){

  var popup=document.getElementById(windowPopup);
  if(popup != null){
	if(windowPopup == 'popupVideo'){
		popup.innerHTML="";
	}
	popup.style.display='none';
  }
  var filter=document.getElementById("shadowFilter");
  if(filter != null){
	filter.style.display='none';
  }
  var chart;
  for(var i=0;i<5;++i){
	  chart=document.getElementById("chartdiv"+i);
	  if(chart != null){
		chart.style.display='block';
	  }else{
	  	break;
	  }
  }
  chart=document.getElementById("chartdiv");
  if(chart != null){
	chart.style.display='block';
  }
}

function popupWinOpenGeneric(popupWindow){
  var de = document.documentElement;
  if(popupWindow == null) popupWindow="popupMsg";
  var popup=document.getElementById(popupWindow);
  var exitWin;
  var winSize;
  var allowLines;
  var popupPad;

  winSize=document.documentElement.clientHeight;



  if(popup != null){
	popup.style.display='block';
	popup.style.marginTop=(popup.clientHeight/2)*-1+"px";
	popup.style.marginLeft=(popup.clientWidth/2)*-1+"px";
	//alert(popup.clientWidth+" height: "+popup.clientHeight);
	windowPopup=popupWindow;
	popup.focus();
  }
  var filter=document.getElementById("shadowFilter");
  if(filter != null){
	filter.style.height= document.body.clientHeight +"px";
	filter.style.display='block';
	filter.style.filter = "alpha(opacity=60)";
	filter.onclick=function(){
		popupWinClose();
	}
  }
  //alert(document.body.clientHeight+" height: "+document.documentElement.clientHeight+" width: "+document.documentElement.clientWidth );
  var chart;
  for(var i=0;i<5;++i){
	  chart=document.getElementById("chartdiv"+i);
	  if(chart != null){
		chart.style.display='none';
	  }else{
	  	break;
	  }
  }
  chart=document.getElementById("chartdiv");
  if(chart != null){
	chart.style.display='none';
  }
}

function popupWinOpen(popupWindow){
  var de = document.documentElement;
  if(popupWindow == null) popupWindow="popupMsg";
  var popup=document.getElementById(popupWindow);
  var exitWin;
  var winSize;
  var allowLines;
  var popupPad;

  winSize=document.documentElement.clientHeight;


  allowLines=parseInt((winSize-70)/40-1);
  allowLines=pageAgencySelection-allowLines;
  if(allowLines<0) allowLines=0;
  popupPad=winSize-(pageAgencySelection*40+160+allowLines*20);
  popupPad=popupPad/2;
  //alert(winSize+"  "+allowLines+" lines: "+pageAgencySelection+" Padding: "+popupPad);

  if(popup != null){
	//e.innerHTML=exitWin;
	popup.style.display='block';
	popup.style.marginTop=(winSize/2*-1+popupPad)+"px";
	windowPopup=popupWindow;
	popup.focus();
  }
  var filter=document.getElementById("shadowFilter");
  if(filter != null){
	filter.style.height= document.body.clientHeight +"px";
	filter.style.display='block';
	filter.style.filter = "alpha(opacity=60)";
	filter.onclick=function(){
		popupWinClose();
	}
  }
  //alert(document.body.clientHeight+" height: "+document.documentElement.clientHeight+" width: "+document.documentElement.clientWidth );
  var chart;
  for(var i=0;i<5;++i){
	  chart=document.getElementById("chartdiv"+i);
	  if(chart != null){
		chart.style.display='none';
	  }else{
	  	break;
	  }
  }
  chart=document.getElementById("chartdiv");
  if(chart != null){
	chart.style.display='none';
  }
}

function getScreenFY(){
var fiscalYear="";
var prefix="";


	if(advanceSearchEnable){
		prefix="a";
	}else{
		prefix="";
	}
	for(var i=2008;i<2016;++i){
		x=document.getElementById(prefix+"FY"+i);
		if(x != null){
			if(x.checked){
				if(fiscalYear != "") fiscalYear+="&";
				fiscalYear+="requestYear="+i;
				//break;
			}
		}
	}
	x=document.getElementById(prefix+"ALL");
	if(x != null){
		if(x.checked){
			fiscalYear="requestYear=2008&requestYear=2009&requestYear=2010&requestYear=2011&requestYear=2012&requestYear=2013&requestYear=2014";
      fiscalYear+="&requestYear=2015"
		}
	}
	return(fiscalYear);
}

function getScreenAgency(){
var strAgencies="";
var agencyName="";

	if(advanceSearchEnable){
		x=document.getElementById("agencyList");
		if(x != null){
			if(x.selectedIndex>1){
			strAgencies+="&";
			strAgencies+="agencyName=";
			strAgencies+=x.options[x.selectedIndex].value;
			}

		}
	}else{
		for(var i=1;i<noAgency+1;++i){
			x=document.getElementById("agency"+i);
			if(x.value == agencies[0]){
				strAgencies="";
				break;
			}
			if(x.value != ""){
				for(var j=0;j<agencies.length;++j){
					if(x.value.toLowerCase() == agencies[j].toLowerCase()){
						agencyName=agenciesAb[j];
						break;
					}
				}
				//if(i != 1) strAgencies+="&";
				strAgencies+="&";
				strAgencies+="agencyName=";
				strAgencies+=agencyName;

			}
		}
		//if(advanceSearchEnable){
		//	prefix="a";
		//}else{
		//	prefix="";
		//}
	}

	return(strAgencies);
}

function jmpURL(){

  document.location=exitUrl;
}

function showPageSize(){
  var de = document.documentElement;
  alert("innerwidth="+window.innerWidth+"Selfinnerwidth="+self.innerWidth+"clientwidth="+(de&&de.clientWidth)+"bodywidth="+document.body.clientWidth);
  alert("innerwidth="+window.innerHeight+"innerwidth="+self.innerHeight+"innerwidth="+(de&&de.clientHeight)+"innerwidth="+document.body.clientHeight);
}


function getCheckedComponents(range){
var mapFoiaReport=[0,1,4,5,12,28,21,22,30,2,3,15,
		0,6,7,8,9,10,11,
		13,14,14,14,15,16,32,
		23,24,25,26,27,18];
var mapFoiaPs=[12,13,14,14,14,15,16];

	var x=document.getElementById("checkedComponents");
	//var ret="compare.html?";
	var ret="";
	if(range == null) range=1;
	//ret+="requestYear=";
	//ret+=getScreenFY();
	ret+="compareRange=";
	//if(range == 4){
		//ret+=mapFoiaPs[selectionPs];
		//ret+="&calculateMethod=";
		//ret+=selectionPs-1;
	//}
	//else{
		ret+=mapFoiaReport[range];
		if(range>19 && range<23){
			ret+="&calculateMethod=";
			ret+=(range-19);
		}
	//}

	//compose yearCompId String
	for(var i=0;i<x.length;i++){
	  if(x.elements[i].type == "checkbox"){
	  	if(x.elements[i].checked){
		  	ret+="&fyCompId=";
		  	ret+=x.elements[i].name;
	  	}
	  }
	}
	//alert(ret);
	//window.open(ret,"FoiaCompare");	//open another window to browse
	compareRequest(ret);

}

function showDiv(division){
	var x=document.getElementById(division);
	if(x != null){
		x.style.display='block';
	}

}

function hideDiv(division){
	var x=document.getElementById(division);
	if(x != null){
		x.style.display='none';
	}

}

function addAgencyBox(division){

  var x;
  var y;
  var z;
  /*for(var i=1;i<division+2;++i){
  	x=document.getElementById("agencydiv"+i);
  	if(x != null){
		if(x.style.display=='none'){
			x.style.display='block';
  			//y=document.getElementById("createReport");
  			//if(y != null){
  			//	y.setAttribute("class","createReport1");
  			//}
			break;
		}
  	}else{
  		alert("no more agency could be selected.");
  	}
  }*/

  z=document.getElementById("addagency"+division);
  if(z != null){
  	if(z.className == "addAgency"){
  		z.className='deleteAgency';
		x=document.getElementById("agencydiv"+(division+1));
		if(x != null){
			x.style.display='block';
		}
  	}else{
  		z.className='addAgency';
		x=document.getElementById("agencydiv"+(division+1));
		if(x != null){
			x.style.display='none';
		}
		y=document.getElementById("agency"+(division+1));
		if(y != null){
			y.value='';
		}
  	}
  }
}
