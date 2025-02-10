// This file contains the JavaScript code that uses D3.js to fetch stock data from stocks.json, process it, and create visualizations such as charts or graphs.

const svgWidth = 800;
const svgHeight = 400;

const svg = d3.select("body")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);

d3.json("data/stocks.json").then(data => {
    const stockData = data.stocks;

    // Process the data as needed
    const xScale = d3.scaleBand()
        .domain(stockData.map(d => d.symbol))
        .range([0, svgWidth])
        .padding(0.1);

    const yScale = d3.scaleLinear()
        .domain([0, d3.max(stockData, d => d.price)])
        .range([svgHeight, 0]);

    // Create bars
    svg.selectAll("rect")
        .data(stockData)
        .enter()
        .append("rect")
        .attr("x", d => xScale(d.symbol))
        .attr("y", d => yScale(d.price))
        .attr("width", xScale.bandwidth())
        .attr("height", d => svgHeight - yScale(d.price))
        .attr("fill", "steelblue");

    // Add axes
    svg.append("g")
        .attr("transform", `translate(0, ${svgHeight})`)
        .call(d3.axisBottom(xScale));

    svg.append("g")
        .call(d3.axisLeft(yScale));
}).catch(error => {
    console.error("Error fetching stock data:", error);
});