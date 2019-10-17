<template>
<div class="container" style="margin: auto">
 <Signup></Signup>
</div>
</template>

<script>
import Signup from '../components/Signup'
export default {
  name: 'RegisterPage',
  components: {
    Signup
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