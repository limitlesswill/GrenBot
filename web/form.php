<?php
$title = "";
$content = "";
$html = '
<form align="center" method="post"
onsubmit = "send();return;">

<input required name="title" 
type="text"/>
<input required name="content" 
type="text"/>

</form>
';
echo $html;
?>
