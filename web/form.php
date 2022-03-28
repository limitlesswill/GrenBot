<?php

$html = '
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" 
content="width=device-width,
initial-scale=1.0">
<title>Form Sweet Form</title>
</head>
<body align ="center" style=
"color:black;background-color:white;">

<form method="get" autocomplete="off" 
align="center">

<table align="center">
<tr>
<td>Title</td>
<td> 
<input type="text" name="title" 
placeholder="Place your title here"/>
</td>
</tr>
<tr>
<td>Content</td>
<td>     
<input type="text" name="content" 
placeholder="place your content here"/>
</td>
</tr> 
</table>
<input type="submit" value="Submit"/>
</form>

<br/><br/>
<a href="index.php"
style="text-decoration:none;">
Go Home</a>
</body>
</html>
';

echo $html;

if( isset($_GET['title']) )
{
     echo "<br/><br/>".$_GET['title']
."<br/><br/><br/>".$_GET['content'];
}
?>
