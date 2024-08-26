/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { CarOut } from './CarOut';
import type { CarType } from './CarType';

export type CarsOut = {
    model?: (string | null);
    license_plate?: (string | null);
    year?: (number | null);
    color?: (string | null);
    photo?: (string | null);
    capacity?: (number | null);
    type?: (CarType | null);
    driver_id: number;
    data: Array<CarOut>;
    count: number;
};

