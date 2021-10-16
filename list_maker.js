
function default_weights() {

    d3.json("http://127.0.0.1:5000/weight").then(function(test) {

    var weights = test;

    d3.select("#weight_class")
        .selectAll("option")
        .data(weights)
        .enter()
        .append("option")
        .text(function(d){return d.name})
        .attr("value", function(d) {return d.name})
        .attr("id", function(d) {return d.name})


    var dropdownMenu = d3.select("#weight_class option:checked").property("value");
    
    d3.json(`http://127.0.0.1:5000/${dropdownMenu}`).then(function(data) {
    
    var fighters = data;

    fighters = fighters.sort(function (a,b) {return d3.ascending(a.name, b.name);});
    
    d3.select("#fighter_1")
            .selectAll("option")
            .data(fighters)
            .enter()
            .append("option")
            .text(function(d){return d.name})
            .attr("value", function(d) {return d.name})
            .attr("id", function(d) {return d.name})
            
    d3.select("#fighter_2")
        .selectAll("option")
        .data(fighters)
        .enter()
        .append("option")
        .text(function(d){return d.name})
        .attr("value", function(d) {return d.name})
        .attr("id", function(d) {return d.name})


    var fighter = d3.select("#fighter_1 option:checked").property("text");

    var fighter_1 = data.filter(item => {
        return item.name == fighter;
    });

    d3.select('#fighter_1_title')
        .selectAll('h3')
        .data(fighter_1)
        .enter()
        .append('h3')
        .text(function(d){return d.name})
        .attr("value", function(d) {return d.name})
        .attr("id", function(d) {return d.name})

    d3.select('#fighter_1_text')
        .selectAll('li')
        .data(fighter_1)
        .enter()
        .append('li')
        .text(function(d){return d.SApM})
        .attr("value", function(d) {return d.SApM})
        .attr("id", "fighter_1_SApM")

    });

    })





};

default_weights();



d3.selectAll("#weight_class").on("change", updateFighters)


function updateFighters() {

    var dropdownMenu = d3.select("#weight_class option:checked").property("text");

    // console.log(dropdownMenu);
    
    d3.json(`http://127.0.0.1:5000/${dropdownMenu}`).then(function(data) {

    var fighters = data;

    d3.select("#fighter_1")
        .selectAll("option")
        .data([])
        .exit()
        .remove()

    d3.select("#fighter_1")
        .selectAll("option")
        .data(fighters)
        .enter()
        .append("option")
        .text(function(d){return d.name})
        .attr("value", function(d) {return d.name})
        .attr("id", function(d) {return d.name})
        
    d3.select("#fighter_2")
        .selectAll("option")
        .data([])
        .exit()
        .remove()

    d3.select("#fighter_2")
        .selectAll("option")
        .data(fighters)
        .enter()
        .append("option")
        .text(function(d){return `${k}: ${v}`})
        .attr("value", function(k, v) {return `${k}: ${v}`})
        .attr("id", function(k, v) {return `${k}: ${v}`})
    })
};



