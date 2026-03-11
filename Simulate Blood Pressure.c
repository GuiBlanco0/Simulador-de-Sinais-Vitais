#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>
#include <string.h>

char state[20] = "rest";
int counter = 0;

/* Random float between min and max */
float rand_range(float min, float max){
    return min + ((float)rand()/RAND_MAX) * (max-min);
}

/* Sensors */

void read_blood_pressure(float *systolic, float *diastolic){

    if(strcmp(state,"rest")==0){
        *systolic = rand_range(115,125);
        *diastolic = rand_range(75,85);
    }

    else if(strcmp(state,"exercise")==0){
        *systolic = rand_range(150,165);
        *diastolic = rand_range(80,90);
    }

    else{
        *systolic = rand_range(130,140);
        *diastolic = rand_range(80,88);
    }
}

float read_temperature(){

    if(strcmp(state,"rest")==0)
        return rand_range(36.5,36.9);

    if(strcmp(state,"exercise")==0)
        return rand_range(37.2,37.6);

    return rand_range(36.9,37.2);
}

float read_spo2(){

    if(strcmp(state,"exercise")==0)
        return rand_range(95,97);

    return rand_range(97,99);
}

int read_heart_rate(){

    if(strcmp(state,"rest")==0)
        return rand()%20 + 60;

    if(strcmp(state,"exercise")==0)
        return rand()%40 + 120;

    return rand()%20 + 90;
}

/* Health condition detection */

char* detect_condition(float systolic, float diastolic, float temp, float spo2, int bpm){

    if(spo2 < 92)
        return "ALERT: Low blood oxygen";

    if(systolic > 160 && diastolic > 100)
        return "ALERT: High blood pressure";

    if(bpm > 110 && systolic > 140 && temp > 37)
        return "Exercise detected";

    if(bpm < 90 && systolic < 130)
        return "Resting state";

    return "Monitoring";
}

/* Main */

int main(){

    srand(time(NULL));

    while(1){

        counter++;

        if(counter == 12)
            strcpy(state,"exercise");

        if(counter == 28)
            strcpy(state,"recovery");

        if(counter == 45){
            strcpy(state,"rest");
            counter = 0;
        }

        float systolic, diastolic;
        float temperature;
        float spo2;
        int bpm;

        read_blood_pressure(&systolic,&diastolic);
        temperature = read_temperature();
        spo2 = read_spo2();
        bpm = read_heart_rate();

        char *status = detect_condition(systolic,diastolic,temperature,spo2,bpm);

        printf("\n==============================\n");
        printf("     WEARABLE HEALTH MONITOR\n");
        printf("==============================\n");
        printf("BP   : %.0f / %.0f mmHg\n", systolic, diastolic);
        printf("HR   : %d BPM\n", bpm);
        printf("TEMP : %.2f C\n", temperature);
        printf("SpO2 : %.1f %%\n", spo2);
        printf("------------------------------\n");
        printf("STATUS: %s\n", status);
        printf("==============================\n");

        sleep(1);
    }

    return 0;
}