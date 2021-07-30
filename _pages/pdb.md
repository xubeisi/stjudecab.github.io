---
title: "pdb"
layout: jmollay
excerpt: "pdb."
sitemap: true
permalink: /pdb/
---

<script>
$(document).ready(function(){

$('#JmolDiv').html( Jmol.getAppletHtml(myJmol, JmolInfo) );
Jmol.jmolCheckbox(myJmol, "spin on", "spin off", "spin");
Jmol.script(myJmol, 'load /assets/jmol/split_FBXW7-204_FBXW7_707.e2e.pdb; cartoon only; color cartoon structure; set echo top left; echo "FBXW7"');

$('#JmolDiv2').html( Jmol.getAppletHtml(myJmol2, JmolInfo2) );
Jmol.jmolCheckbox(myJmol2, "spin on", "spin off", "spin");
Jmol.script(myJmol2, 'load https://alphafold.ebi.ac.uk/files/AF-Q969H0-F1-model_v1.pdb; cartoon only; color cartoon structure; set echo top left; echo "Alphafold"');

}
);
</script>

<div class="row">
<div class="col-sm-6 clearfix">
<span id="span_jmolCheckbox0"><input type="checkbox" name="jmolCheckbox0" id="jmolCheckbox0" onclick="Jmol.controls._cbClick(this)" onmouseover="Jmol.controls._cbOver(this);return true" onmouseout="Jmol.controls._mouseOut()"><label for="jmolCheckbox0">Spin</label></span>
<div id="JmolDiv" style="width:70vmin; height:70vmin;"></div>
</div>
<div class="col-sm-6 clearfix">
<span id="span_jmolCheckbox1"><input type="checkbox" name="jmolCheckbox1" id="jmolCheckbox1" onclick="Jmol.controls._cbClick(this)" onmouseover="Jmol.controls._cbOver(this);return true" onmouseout="Jmol.controls._mouseOut()"><label for="jmolCheckbox1">Spin</label></span>
<div id="JmolDiv2" style="width:70vmin; height:70vmin;"></div>
</div>
</div>
