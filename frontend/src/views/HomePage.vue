<template>
<div class="container" style="margin: auto">
<DiaryList></DiaryList>
</div>
</template>

<script>
import DiaryList from '../components/DiaryList'
export default {
  name: 'HomePage',
  components: {
  DiaryList
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