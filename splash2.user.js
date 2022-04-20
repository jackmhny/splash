// ==UserScript==
// @name        Splash
// @namespace   https://github.com/jackmhny/splash/
// @match       https://*.veracross.com/*
// @grant       none
// @version     1.0
// @author      someone
// @description Spluck Fash
// @require https://cdn.jsdelivr.net/npm/@violentmonkey/dom@1
// @require https://cdn.jsdelivr.net/npm/jquery@3/dist/jquery.min.js
// ==/UserScript==


function isLetter(str) {
  return str.length === 1 && str.match(/[a-z]/i);
}

$( function() {
  if(window.location.pathname == '/lville/student/student/overview') {
  console.log("hi!")
  classLinks = $(".website-link")
  classLinkCount = classLinks.length
  directoryLinkCount = classLinkCount / 3
  directoryLinks = []
  for(let i = 0; i < 6 && i < directoryLinkCount; i++) {
    console.log(classLinks[3*i+2])
    classLinks[3*i+2].click()
  }
  
  
} else {
  

// LA443S.2.B: Latin 3
// ["LA443S.2.B", " Latin 3"]
classHeader = $(".class-header > > a").text().split(":")
// ".B"
classHeaderEnd = classHeader[0].substring(classHeader[0].length-2,classHeader[0].length)
// "Latin 3"
className = classHeader[1].trim()
// If there is a class period letter at the end of the identification segment, extract it
if(classHeaderEnd[0] == "." && isLetter(classHeaderEnd[1])){
  classPeriod = classHeaderEnd[1]
}
else {
  classPeriod = "X"
}

names=$(".directory-Entry_Title").text().replaceAll(" ","").replaceAll("\n\n","\n").trim().split("\n")

teacherName = $("h4").text()

console.table({classPeriod, className, teacherName, names})
$.ajax("https://splashflask.vercel.app/", {
    data : JSON.stringify({className, classPeriod, teacherName, names}),
    contentType : 'application/json',
    type : 'POST',
})

}
});
