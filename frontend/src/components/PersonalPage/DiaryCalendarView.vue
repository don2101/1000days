<template>
    <v-row class="fill-height">
        <v-col>
            <v-sheet height="64">
                <v-toolbar flat color="white">
                    <v-btn outlined class="mr-4" @click="setToday">
                        Today
                    </v-btn>
                    <v-btn fab text small @click="prev">
                        <v-icon small>mdi-chevron-left</v-icon>
                    </v-btn>
                    <v-btn fab text small @click="next">
                        <v-icon small>mdi-chevron-right</v-icon>
                    </v-btn>
                    <v-toolbar-title>{{ title }}</v-toolbar-title>
                    <v-spacer></v-spacer>
                    <v-menu bottom right>
                        <template v-slot:activator="{ on }">
                            <v-btn
                                    outlined
                                    v-on="on"
                            >
                                <span>{{ typeToLabel[type] }}</span>
                                <v-icon right>mdi-menu-down</v-icon>
                            </v-btn>
                        </template>
                        <v-list>
                            <v-list-item @click="type = 'day'">
                                <v-list-item-title>Day</v-list-item-title>
                            </v-list-item>
                            <v-list-item @click="type = 'week'">
                                <v-list-item-title>Week</v-list-item-title>
                            </v-list-item>
                            <v-list-item @click="type = 'month'">
                                <v-list-item-title>Month</v-list-item-title>
                            </v-list-item>
                            <v-list-item @click="type = '4day'">
                                <v-list-item-title>4 days</v-list-item-title>
                            </v-list-item>
                        </v-list>
                    </v-menu>
                </v-toolbar>
            </v-sheet>
            <v-sheet height="600">
                <v-calendar
                        ref="calendar"
                        v-model="focus"
                        color="primary"
                        :events="events"
                        :event-color="getEventColor"
                        :event-margin-bottom="3"
                        :now="today"
                        :type="type"
                        @click:event="showEvent"
                        @click:more="viewDay"
                        @click:date="viewDay"
                        @change="updateRange"
                ></v-calendar>
                <v-menu
                        v-model="selectedOpen"
                        :close-on-content-click="false"
                        :activator="selectedElement"
                        full-width
                        offset-x
                >
                    <v-card
                            color="grey lighten-4"
                            min-width="350px"
                            flat
                    >
                        <v-toolbar
                                :color="selectedEvent.color"
                                dark
                        >
                            <v-btn icon>
                                <v-icon>mdi-pencil</v-icon>
                            </v-btn>
                            <v-toolbar-title v-html="selectedEvent.name"></v-toolbar-title>
                            <v-spacer></v-spacer>
                            <v-btn icon>
                                <v-icon>mdi-heart</v-icon>
                            </v-btn>
                            <v-btn icon>
                                <v-icon>mdi-dots-vertical</v-icon>
                            </v-btn>
                        </v-toolbar>
                        <v-card-text>
                            <span v-html="selectedEvent.details"></span>
                        </v-card-text>
                        <v-card-actions>
                            <v-btn
                                    text
                                    color="secondary"
                                    @click="selectedOpen = false"
                            >
                                Cancel
                            </v-btn>
                        </v-card-actions>
                    </v-card>
                </v-menu>
            </v-sheet>
        </v-col>
    </v-row>
</template>

<script>
    export default {
        data() {
            return {
                today: '2019-10-25',
                focus: '2019-10-25',
                type: 'month',
                typeToLabel: {
                    month: 'Month',
                    week: 'Week',
                },
                start: null,
                end: null,
                selectedEvent: {},
                selectedElement: null,
                selectedOpen: false,
                events: [
                    {
                        name: 'D+224',
                        details: '224일째~~~!',
                        start: '2019-10-19',
                        end: '2019-10-19',
                        color: 'yellow',
                    },
                    {
                        name: 'D+223',
                        details: '223일째~~~!',
                        start: '2019-10-18',
                        end: '2019-10-18',
                        color: 'indigo',
                    },
                    {
                        name: 'D+222',
                        details: '222일째~~~!',
                        start: '2019-10-17',
                        end: '2019-10-17',
                        color: 'deep-purple',
                    },
                    {
                        name: 'D+221',
                        details: '221일째~~~!',
                        start: '2019-10-16',
                        end: '2019-10-16',
                        color: 'cyan',
                    },
                    // {
                    //   name: 'D+224',
                    //   details: '224일째~~~!',
                    //   start: '2019-10-19',
                    //   end: '2019-10-19',
                    //   color: 'red',
                    // },
                    // {
                    //   name: 'D+224',
                    //   details: '224일째~~~!',
                    //   start: '2019-10-19',
                    //   end: '2019-10-19',
                    //   color: 'brown',
                    // },
                    // {
                    //   name: 'D+224',
                    //   details: '224일째~~~!',
                    //   start: '2019-10-19',
                    //   end: '2019-10-19',
                    //   color: 'blue',
                    // },
                    // {
                    //   name: 'D+224',
                    //   details: '224일째~~~!',
                    //   start: '2019-10-19',
                    //   end: '2019-10-19',
                    //   color: 'deep-orange',
                    // },
                    // {
                    //   name: 'D+224',
                    //   details: '224일째~~~!',
                    //   start: '2019-10-19',
                    //   end: '2019-10-19',
                    //   color: 'teal',
                    // },
                    // {
                    //   name: 'D+224',
                    //   details: '224일째~~~!',
                    //   start: '2019-10-19',
                    //   end: '2019-10-19',
                    //   color: 'green',
                    // },
                    // {
                    //   name: 'D+224',
                    //   details: '224일째~~~!',
                    //   start: '2019-10-19',
                    //   end: '2019-10-19',
                    //   color: 'grey darken-1',
                    // },
                ],
            }
        },
        computed: {
            title() {
                const {start, end} = this
                if (!start || !end) {
                    return ''
                }

                const startMonth = this.monthFormatter(start)
                const endMonth = this.monthFormatter(end)
                const suffixMonth = startMonth === endMonth ? '' : endMonth

                const startYear = start.year
                const endYear = end.year
                const suffixYear = startYear === endYear ? '' : endYear

                const startDay = start.day + this.nth(start.day)
                const endDay = end.day + this.nth(end.day)

                switch (this.type) {
                    case 'month':
                        return `${startMonth} ${startYear}`
                    case 'week':
                    case '4day':
                        return `${startMonth} ${startDay} ${startYear} - ${suffixMonth} ${endDay} ${suffixYear}`
                    case 'day':
                        return `${startMonth} ${startDay} ${startYear}`
                }
                return ''
            },
            monthFormatter() {
                return this.$refs.calendar.getFormatter({
                    timeZone: 'UTC', month: 'long',
                })
            },
        },
        mounted() {
            this.$refs.calendar.checkChange()
        },
        methods: {
            viewDay({date}) {
                this.focus = date
                this.type = 'day'
            },
            getEventColor(event) {
                return event.color
            },
            setToday() {
                this.focus = this.today
            },
            prev() {
                this.$refs.calendar.prev()
            },
            next() {
                this.$refs.calendar.next()
            },
            showEvent({nativeEvent, event}) {
                const open = () => {
                    this.selectedEvent = event
                    this.selectedElement = nativeEvent.target
                    setTimeout(() => this.selectedOpen = true, 10)
                }

                if (this.selectedOpen) {
                    this.selectedOpen = false
                    setTimeout(open, 10)
                } else {
                    open()
                }

                nativeEvent.stopPropagation()
            },
            updateRange({start, end}) {
                // You could load events from an outside source (like database) now that we have the start and end dates on the calendar
                this.start = start
                this.end = end
            },
            nth(d) {
                return d > 3 && d < 21
                    ? 'th'
                    : ['th', 'st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th'][d % 10]
            },
        },
    }
</script>