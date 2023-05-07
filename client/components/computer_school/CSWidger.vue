<template>
    <div>
        <script defer src="https://vk.com/js/api/openapi.js?169" type="text/javascript" ></script>
        <div id="vk_groups"></div>
        <script defer type="text/javascript">
            VK.Widgets.Group("vk_groups", {mode: 1, width: "220", height: "400"}, 59236669)
        </script>
        
        <script defer type="text/javascript">
            VK.Widgets.CommunityMessages("vk_community_messages", 59236669, {tooltipButtonText: "Есть вопрос?", expanded: 0})
        </script>
        <script defer type="text/javascript">
            VK.init({
                apiId: "dda84ff491c4ab15f5aacb812db61f098211594c7e584bacb3b02ec88b907872dba411c191cad2b91e398",
                onlyWidgets: false
            })
        </script>  
    </div>
</template>
<script>
export default {
    beforeCreate() {
        
    },
}
</script>
