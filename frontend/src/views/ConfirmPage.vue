<template>
<div class="container" style="margin: auto">
<Passwordconfirm></Passwordconfirm>
</div>
</template>


<script>
import Passwordconfirm from '../components/Passwordconfirm'
export default {
  name: 'AccountPage',
   data: () => ({
    }),
  components: {
    Passwordconfirm
  },
  methods: {
  }
  }
</script>
<style>
  .container {
      width: 70%;
}
</style>