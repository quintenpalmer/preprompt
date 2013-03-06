$module = {
    __getattr__ : function(attr){
        if(attr==="stdout"){return document.$stdout}
        if(attr==="stderr"){return document.$stderr}
        else{return $getattr(this,attr)}
        },
    __setattr__ : function(attr,value){
        if(attr==="stdout"){document.$stdout=value}
        if(attr==="stderr"){document.$stderr=value}
        },
    has_local_storage:typeof(Storage)!=="undefined",
    has_json:typeof(JSON)!=="undefined",
    version_info:[1,1,"20130304-221651"],
    path:[]
}
