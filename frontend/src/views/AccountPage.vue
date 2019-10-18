<template>
<div class="container" style="margin: auto">
<div v-if="userInfo=='null'">
<Error></Error>
fail
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
    ...mapState({
        userInfo: state => state.moduleName.userInfo
        }),
        }
  }
</script>
<style>
.container{
   width: 70%;
}
</style>