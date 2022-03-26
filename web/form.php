<?php
$title = "";
$content = "";

function send()
{
global $title;
global $content;
echo $title;
echo "<br/><br/>".$content;
}

$html = '
<body align ="center" style=
"color:black;background-color:white;">

<form align="center" method="post"
onsubmit = "send();return;">

<table align="center">
<tr>
<td>Title</td>
<td>      
<input size="25"
type="text" name="title"
placeholder="Place your title here">
</td>
</tr>
<tr>
<td>Content</td>
<td>     
<input size="25"
type="text" name="content"
placeholder="place your content here">
</td>
</tr> 
</table>
<input type="submit" value="Submit"/>

</form>

</body>
';


echo $html;

?>
