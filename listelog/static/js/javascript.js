
function writep(h1,p1,x)
{
var elms=document.getElementsByName("link");
var n = elms.length;
for(var i=0;i<n;i++)
{
if(i==x)
{
if(elms[i].style.borderStyle == "inset")
{
document.getElementById("right").style.visibility = "hidden";
document.getElementById("plus").style.visibility = "hidden";
elms[i].style.borderStyle = "outset";
}
else
{
	for(var j=0;j<n;j++)
{

document.getElementById("right").style.visibility = "hidden";
document.getElementById("plus").style.visibility = "hidden";
elms[j].style.borderStyle = "outset";
}
document.getElementById("right").style.visibility = "visible";
document.getElementById("demoh1").innerHTML = h1;
document.getElementById("demo").innerHTML = p1;
document.getElementById("right").style.borderStyle = "solid";
elms[i].style.borderStyle = "inset";
}
}
}

}

function closep()
{
var elms=document.getElementsByName("link");
var n = elms.length;
	for(var j=0;j<n;j++)
{

document.getElementById("right").style.visibility = "hidden";
document.getElementById("plus").style.visibility = "hidden";
elms[j].style.borderStyle = "outset";
}
document.getElementById("addon").style.visibility = "hidden";
document.getElementById("addon").innerHTML = "";
}


function showp(tab)
{
i=0;
document.getElementById("aleft").style.visibility="hidden";
document.getElementById("aright").style.visibility="visible";
document.getElementById("diap").style.display = "block";
document.body.style.overflow = "hidden";
document.getElementById("diapimag").innerHTML='<img id="imgdiap" src="'+tab[i]+'">';

document.getElementById("aleft").addEventListener("click",function(){if(i>0){i--;}
document.getElementById("diapimag").innerHTML='<img id="imgdiap" src="'+tab[i]+'">';if(i<=0)
{
document.getElementById("aleft").style.visibility="hidden";
}
else
{
	document.getElementById("aleft").style.visibility="visible";
}

if(i==tab.length-1)
{
document.getElementById("aright").style.visibility="hidden";
}
else
{
	document.getElementById("aright").style.visibility="visible";
}});

document.getElementById("aright").addEventListener("click",function(){if(i<tab.length-1){i++;}document.getElementById("aright").style.visibility="hidden";
document.getElementById("diapimag").innerHTML='<img id="imgdiap" src="'+tab[i]+'">';if(i<=0)
{
document.getElementById("aleft").style.visibility="hidden";
}
else
{
	document.getElementById("aleft").style.visibility="visible";
}

if(i==tab.length-1)
{
document.getElementById("aright").style.visibility="hidden";
}
else
{
	document.getElementById("aright").style.visibility="visible";
}});


}

function quit()
{
	document.getElementById("diap").style.display = "none";
}

function quit0()
{
	document.getElementById("diap0").style.display = "none";
}

function exco()
{

	if(document.getElementById("right").style.visibility == "hidden")
	{
		document.getElementById("right").style.visibility = "visible";
		document.getElementById("plus").style.visibility = "hidden";
		document.getElementById("addon").style.visibility = "visible";
	}
	else
	{
		document.getElementById("right").style.visibility = "hidden";
		document.getElementById("plus").style.visibility = "visible";
		document.getElementById("addon").style.visibility = "hidden";
	}
}

function addon(parce)
{
	if(document.getElementById("addon").innerHTML=="")
	{
	document.getElementById("addon").style.visibility = "visible";
	document.getElementById("addon").innerHTML = parce;
	}
	else
	{
		document.getElementById("addon").style.visibility = "hidden";
		document.getElementById("addon").innerHTML = "";
	}
}
