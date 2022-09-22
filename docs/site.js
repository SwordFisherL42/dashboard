var csv;
var ids;
var ids_link = "./tracked_ids"
var csv_link = "https://staticstats.nexusmods.com/live_download_counts/mods/2673.csv";
function httpGetAsync(resourceUri, callback)
{
    let xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", resourceUri, true);
    xmlHttp.send(null);
}
function get_totals(csvArray, idList){
    let unique_dl = 0;
    let total_dl = 0;
    let total_views = 0;
    let total_mods = 0;
    for (let i=0; i<csvArray.length; i++){
        if (idList.includes(csvArray[i][0])){
            total_mods += 1
            total_dl += Number(csvArray[i][1])
            unique_dl += Number(csvArray[i][2])
            total_views += Number(csvArray[i][3])
        }
    }
    console.log(`Total Downloads: ${total_dl}, Unique Downloads: ${unique_dl}, Page Views: ${total_views}`)
    document.getElementById("total-mods").innerHTML = total_mods;
    document.getElementById("unique-dl").innerHTML = unique_dl.toLocaleString('en', {useGrouping:true});
    document.getElementById("total-dl").innerHTML = total_dl.toLocaleString('en', {useGrouping:true});
    document.getElementById("page-views").innerHTML = total_views.toLocaleString('en', {useGrouping:true});
    document.getElementById("copy-year").innerHTML = new Date().getFullYear();
}
function parseHttpCsv(csvText){
    csv = CSVToArray(csvText, ",");
    httpGetAsync(ids_link, parseHttpTrackedId)
}
function parseHttpTrackedId(trackedIdText){
    ids = trackedIdText.split("\n")
    get_totals(csv, ids)
}
httpGetAsync(csv_link, parseHttpCsv)