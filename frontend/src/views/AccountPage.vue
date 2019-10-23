<template>
<div class="container" style="margin: auto">
<div v-if="checkToken==null">
<Error></Error>
</div>
<div v-else>
<MyInfo></MyInfo>
</div>
</div>
</template>


<script>
import Error from '../components/Error'
import MyInfo from '../components/MyInfo'
import {mapState} from 'vuex'
export default {
  name: 'AccountPage',
   components: {
   Error,
   MyInfo
  },
  methods: {
   },
   computed: {
       checkToken(){
       return sessionStorage.getItem('token')
}
        }
  }
</script>
<style scoped>
.container{
   width: 70%;
}
</style>