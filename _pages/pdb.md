---
title: "pdb"
layout: default
excerpt: "pdb."
sitemap: true
permalink: /pdb/
---

<script src="/assets/jmol/jsmol/JSmol.min.js"></script>

<script>
var pdblistfile = "/assets/jmol/pdb.lst";
var pdblist=[];
var myJmols=[];

const JmolInfo = {
width:'100%',
height:'100%',
color:'#E2F4F5',
j2sPath:'/assets/jmol/jsmol/j2s',
serverURL:'/assets/jmol/jsmol/php/jsmol.php',
use:'html5'
};

fetch(pdblistfile)
.then(response => response.text())
.then(data => {
	var lines = data.trim().split('\n');
	for(var line = 0; line < lines.length; line++){
		if (lines[line].length > 0){
			pdblist.push(lines[line].trim().split(/\s+/));
			myJmols.push('myJmol' + line.toString());
		}
	}
	$(document).ready(function(){
		createTable([["row 1, cell 1", "row 1, cell 2"], ["row 2, cell 1", "row 2, cell 2"]]);
		for(var line = 0; line < pdblist.length; line++){
		var myJmol = myJmols[line];
		var cmds=[];
		var x=pdblist[line][0],
		    y=pdblist[line][1],
		    pdbname=pdblist[line][2],
		    onepdbfile=pdblist[line][3];
		cmds.push(`$('#JmolDiv${x}_${y}').html( Jmol.getAppletHtml('${myJmol}', JmolInfo) );`)
		cmds.push(`Jmol.jmolCheckbox(${myJmol}, "spin on", "spin off", "spin");`)
		cmds.push(`Jmol.script(${myJmol}, 'load ${onepdbfile}; cartoon only; color cartoon structure; set echo top left; echo "${pdbname}"');`)
		cmd = cmds.join("\n")
		console.log(cmd);
		eval(cmd);
		}
	});
});

function createTable(tableData) {
  var table = document.createElement('table');
  var tableBody = document.createElement('tbody');
  var iline = 0, ix = 1, iy = 1;
  tableData.forEach(function(rowData) {
    var row = document.createElement('tr');

    rowData.forEach(function(cellData) {
      var cell = document.createElement('td');
      var celldiv = document.createElement('div');
	  if (cellData.length > 0){
        var cellDatadiv = `<span id="span_jmolCheckbox${iline}"><input type="checkbox" name="jmolCheckbox${iline}" id="jmolCheckbox${iline}" onclick="Jmol.controls._cbClick(this)" onmouseover="Jmol.controls._cbOver(this);return true" onmouseout="Jmol.controls._mouseOut()"><label for="jmolCheckbox${iline}">Spin</label></span>\n`
        cellDatadiv += `<div id="JmolDiv${ix}_${iy}" style="width:70vmin; height:70vmin;"></div>`
        celldiv.innerHTML = cellDatadiv;
        iline += 1;
	  } else {
        celldiv.innerHTML = ""
	  }
	  cell.appendChild(celldiv);
      row.appendChild(cell);
      ix += 1;
    });

    tableBody.appendChild(row);
    iy += 1;
  });

  table.appendChild(tableBody);
  const currentDiv = document.getElementById("AllPDBs");
  currentDiv.appendChild(table);
  
}
</script>

<div id="AllPDBs"></div>
