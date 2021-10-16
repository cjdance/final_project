
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

    });

    })





};

default_weights();



d3.selectAll("#weight_class").on("change", updateFighters)

d3.selectAll("#fighter_1").on("change", updateCard1)

d3.selectAll("#fighter_2").on("change", updateCard2)


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
        .text(function(d){return d.name})
        .attr("value", function(d) {return d.name})
        .attr("id", function(d) {return d.name})
    })
};



function updateCard1() {

    var dropdownMenu = d3.select("#weight_class option:checked").property("text");

    d3.json(`http://127.0.0.1:5000/${dropdownMenu}`).then(function(data) {

        var fighter = d3.select("#fighter_1 option:checked").property("text");

        var fighter_1 = data.filter(item => {
            return item.name == fighter;
        });

        console.log(fighter_1);

        var title = d3.select("#fighter_1_title");
        var list = d3.select("fighter_1_list");
        var text = d3.select("fighter_1_text");

        title.selectAll('h3').data([]).exit().remove();
        list.selectAll("li").data([]).exit().remove();
        text.data([]).exit().remove();

        title.data(fighter_1)
            .selectAll('h3')
            .data(fighter_1)
            .enter()
            .append('h3')
            .text(function(d){return d.name})
            .attr("value", function(d) {return d.name})
            .attr("id", function(d) {return d.name})

        });
      

    }