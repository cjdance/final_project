
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


    })

    })



};

default_weights();



d3.selectAll("#weight_class").on("change", updateFighters)


function updateFighters() {

    var dropdownMenu = d3.select("#weight_class option:checked").property("value");
    
    d3.json(`http://127.0.0.1:5000/${dropdownMenu}`).then(function(data) {

    var fighters = data;

    d3.select("#fighter_1")
        .selectAll("option")
        .data(fighters)
        .enter()
        .append("option")
        .text(function(d){return d.name})
        .attr("value", function(d) {return d.name})
        .attr("id", function(d) {return d.name})
        

    })
};


// d3.json("http://127.0.0.1:5000/featherweight").then((data) => 
//     {
//         data.forEach(element => console.log(element.name))
//     }
    
// );