<?php
$title = "";
$content = "";

$html = '
<body align ="center" style=
"color:black;background-color:white;">

<form align="center" method="post"
onsubmit = "send();return;">

<table>
<tr>
<td>Title</td>
<td>
<input type="text" name="title" size="25">
</td>
</tr>
<tr>
<td>Content</td>
<td>
<input type="text" name="content" size="25">
</td>
</tr> 
</table>
<input type="submit" value="Submit"/>

</form>

</body>
';

function send()
{
global $title , $content;
echo $title;
echo "<br/><br/>".$content;
}

echo $html;

?>
