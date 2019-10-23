<template>
<div class="container" style="margin: auto">
   <Baby></Baby>
   </div>
</template>

<script>
import Baby from '../components/Baby'
  export default {
  name:'BabyInfoPage',
    components:{
        Baby
    },
    methods: {},
  }
</script>
<style scoped>
.container{
   width: 70%;
}
</style>