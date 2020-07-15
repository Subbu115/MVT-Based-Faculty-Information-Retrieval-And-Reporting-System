function parse_json(string_data) {
    var json_data = "[" + string_data.substr(1, string_data.length - 2).split(/\s?,\s?/).map(
        function (v) {
            return v.split(/\s?:\s?/).map(function (p) {
                return p.replace(/'/g, '"');
            }).join(":");
        }).join(",") + "]";
    return json_data;


}
