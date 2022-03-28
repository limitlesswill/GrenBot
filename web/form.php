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

<form method="post" autocomplete="off" 
align="center">

<table align="center">
<tr>  
<td>Title</td>
<td>
<input size="30" required
type="text" name="title" 
placeholder="Place your title here"/>
</td>
</tr>
<tr>
<td>Content</td>
<td>
<textarea rows="3" cols="33"
required name="content" 
placeholder="place your content here">
</textarea>
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

<?php
if( isset($_POST['title']) )
{
echo "<br/><br/><h3>".$_POST['title']
."</h3><br/>".$_POST['content'];
}
?>
