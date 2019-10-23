<template>
<div class="container" style="margin: auto">
<Passwordconfirm></Passwordconfirm>
</div>
</template>


<script>
import Passwordconfirm from '../components/Passwordconfirm'
export default {
  name: 'ConfirmPage',
   data: () => ({
    }),
  components: {
    Passwordconfirm
  },
  methods: {
  }
  }
</script>
<style scoped>
  .container {
      width: 70%;
}
</style>