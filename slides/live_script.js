/*  
this is what I'm going to type in to the Chrome developer console
after having gone through the select / append / selectAll bit in select.html. Won't bother with the semicolons
*/
d3.json('http://localhost:8000/data/meetup_history.json', function(data){d=data})
g = d3.select("body").append("svg");
c = g.selectAll("circle")
c.data(d).enter().append("circle").attr("class","badass")
d3.selectAll("circle.badass").attr("cx", function(d){return (d.time - 1238713200000)/100000000;})
d3.selectAll("circle.badass").attr("cy", function(d){return d.yes_rsvp_count;})
d3.selectAll("circle.badass").attr("r", 6)
d3.selectAll("circle.badass").attr("cy", function(d){return 300-d.yes_rsvp_count;})

