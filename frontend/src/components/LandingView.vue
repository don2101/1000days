<template>
    <div id="fullpage" style="text-align: center; margin-top: 15px">
        <C1/>
        <C2/>
        <C3/>
        <C4/>
    </div>
</template>


<script>
    import {mapActions} from 'vuex'
    import C1 from './LandingViewSections/C1.vue'
    import C2 from './LandingViewSections/C2.vue'
    import C3 from './LandingViewSections/C3.vue'
    import C4 from './LandingViewSections/C4.vue'

    export default {
        name: 'LandingView',
        components: {
          C1, C2, C3, C4
        },
        data() {
            return {
            }
        },
        mounted() {
            new fullpage('#fullpage', {
                //options here
                autoScrolling:true,
                scrollHorizontally: true
            });
        },

    }
</script>

<style>

</style>