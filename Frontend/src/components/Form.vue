<template>
    <div class="hello">
        <b-container>
            <b-row class="justify-content-md-center" cols="10">
                <b-col style="margin-top:25vh;" cols="6">
                    <h2>LOGIN</h2>
                        <b-form @submit="onSubmit" @reset="onReset" v-if="show">
            <b-form-group
                id="input-group-1"
                label="USer:"
                label-for="input-1">
                
                <b-form-input
                    id="input-1"
                    v-model="form.user"
                    type="text"
                    required
                    placehollder="Enter User">
                </b-form-input>
            </b-form-group>

            <b-form-group id="input-froup-2" label="Password:" label-for="input-2">
                <b-form-input
                    id="input-2"
                    v-model="formpassword"
                    type="password"
                required
                placeholder="Enter Password">
                </b-form-input>
            </b-form-group>


            <b-button type="submit" class="mr-4" variant="primary">Submit</b-button>
            <b-button type="reset" variant="danger">Reset</b-button>
            <h6 class="text-danger mt-4" v-if="con">INVALID USER OR PASSWORD</h6>
        </b-form>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
export default {
    name: 'Form',
    data() {
        return {
            form: {
                user: '',
                password: '',
            },
            show: true,
            con:false
        }
    },
    methods: {
        onsubmit(evt) {
            evt.preventDefault()
            if (this.form.user=="admin" && this.form.password=='123456') {
                this.$router.push('about')
            } else{
                this.con=true
            }
        },
        onReset(evt) {
            evt.preventDefault()
            //Reset our form values

            this.form.user = ''
            this.form.password = ''
            this.con=false//Trick to reset/clear native browser form validation state
            this.show = false
            this.$nextTick(() => {
                this.show = true
            })
        }
    }
}
</script>
