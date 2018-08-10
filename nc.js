var zoom = d3.zoom();

// color 
var income_domain = [0, 10000, 25000, 40000, 55000, 70000, 85000, 100000, 150000, 190000] //ranges of income
//min = $9107; max = $190104
var income_color = d3.scaleThreshold()
    .domain(income_domain)
    .range(d3.schemeGreens[9]); //9 shades of green

// incomeData 
var incomeData = d3.map(); //puts all income data into key-value pairs (dict) ==> {id: value}


// asynchronous tasks, load topojson maps and data
d3.queue()
    .defer(d3.json, "cb_2017_37_tract_500k.topojson")
    .defer(d3.csv, "income.csv", function(d) { 
        if (isNaN(d.income)) {
            incomeData.set(d.id, 0); 
        } else {
            incomeData.set(d.id, +d.income); 
        }
        
    })
    .await(ready);//goes to function ready



// callback function  
function ready(error, data) {

    if (error) throw error;

    // north_carolina topojson object
    var north_carolina = topojson.feature(data, {
        type: "GeometryCollection",
        geometries: data.objects.cb_2017_37_tract_500k.geometries //look in topo file, "geometries", "objects":{"cb_2017_37_tract_500k"
    });

    // projection and path
    var projection = d3.geoAlbersUsa()
        .fitExtent([ [20, 20], [500, 800] ], north_carolina); //padding, width and height

    var geoPath = d3.geoPath()
        .projection(projection);

    // draw new york map and bind income data
    d3.select("svg.income").selectAll("path")
        .data(north_carolina.features)
        .enter()
        .append("path")
        .attr("d", geoPath)
        .attr("fill", "white")
        .transition().duration(100)
        .delay(function(d, i) {
            return i * 50; 
        })
        .ease(d3.easeLinear)
        .attr("fill", function(d) { 
            var value = incomeData.get(d.properties.GEOID);
            return (value != 0 ? income_color(value) : "lightblue");  

        })
        .attr("class", "counties-income");
    
    // title
    d3.select("svg.income").selectAll("path")
        .append("title")
        .text(function(d) {
            return d.income = incomeData.get(d.properties.GEOID);
        });
}

