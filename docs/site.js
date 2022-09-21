function httpGetAsync(theUrl, modList, callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText, modList);
    }
    xmlHttp.open("GET", theUrl, true);
    xmlHttp.send(null);
}
function get_totals(csv, id_list){
    var ca = CSVToArray(csv, ",");
    var unique_dl = 0;
    var total_dl = 0;
    var total_views = 0;
    var total_mods = 0;
    for (let i=0; i<ca.length; i++){
        if (id_list.includes(ca[i][0])){
            total_mods += 1
            total_dl += Number(ca[i][1])
            unique_dl += Number(ca[i][2])
            total_views += Number(ca[i][3])
        }
    }
    console.log(`Total Downloads: ${total_dl}, Unique Downloads: ${unique_dl}, Page Views: ${total_views}`)
    document.getElementById("total-mods").innerHTML = total_mods;
    document.getElementById("unique-dl").innerHTML = unique_dl.toLocaleString('en', {useGrouping:true});
    document.getElementById("total-dl").innerHTML = total_dl.toLocaleString('en', {useGrouping:true});
    document.getElementById("page-views").innerHTML = total_views.toLocaleString('en', {useGrouping:true});
    document.getElementById("copy-year").innerHTML = new Date().getFullYear();
}
csv_link = "https://staticstats.nexusmods.com/live_download_counts/mods/2673.csv";
tracked_ids = ['2058', '5819', '5297', '1645', '2142', '6614', '5889', '2556', '5720', '2057', '1110', '6306', '2683', '2555', '4026', '5180', '3067', '5843', '1686', '1613', '1139', '1219', '6302', '2557', '3027', '3066', '5849'];
httpGetAsync(csv_link, tracked_ids, get_totals);