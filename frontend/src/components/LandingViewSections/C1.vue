<template>
    <div class="section">
        <div style="width: 100%; height: 100%;
    background-image: url('../../images/LandingView/holdingHand-black.jpg')">
            <h1>Every Moment with You is Special</h1>
            <button @click="test({'username':'lia'})">clickclickclickclickclickclickclick</button>
        </div>
    </div>
</template>


<script>
    import {mapActions} from 'vuex'
    export default {
        name: 'C1',
        methods: {
            ...mapActions('data', ['test'])
        }

    }
</script>