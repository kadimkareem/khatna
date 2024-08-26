/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { CarType } from './CarType';

export type CarOut = {
    model?: (string | null);
    license_plate?: (string | null);
    year?: (number | null);
    color?: (string | null);
    photo?: (string | null);
    capacity?: (number | null);
    type?: (CarType | null);
    driver_id: number;
    id: number;
};

