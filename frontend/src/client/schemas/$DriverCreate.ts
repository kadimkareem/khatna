/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export const $DriverCreate = {
    properties: {
        license_number: {
            type: 'string',
            isRequired: true,
        },
        license_expiry_date: {
            type: 'string',
            isRequired: true,
            format: 'date-time',
        },
        years_of_experience: {
            type: 'number',
            isRequired: true,
        },
        discription: {
            type: 'string',
            isRequired: true,
        },
    },
} as const;
