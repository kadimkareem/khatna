import React from 'react'
import {
  Button,
  FormControl,
  FormErrorMessage,
  FormLabel,
  Input,
  Modal,
  ModalBody,
  ModalCloseButton,
  ModalContent,
  ModalFooter,
  ModalHeader,
  ModalOverlay,
} from '@chakra-ui/react'
import { SubmitHandler, useForm } from 'react-hook-form'
import { useMutation, useQueryClient } from 'react-query'

import { ApiError, CreateCar, CarsService } from '../../client'
import useCustomToast from '../../hooks/useCustomToast'

interface AddCarProps {
  isOpen: boolean
  onClose: () => void
}

const AddCar: React.FC<AddCarProps> = ({ isOpen, onClose }) => {
  const queryClient = useQueryClient()
  const showToast = useCustomToast()
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<CreateCar>({
    mode: 'onBlur',
    criteriaMode: 'all',
    defaultValues: {
      capacity: 0,
      color: '',
      license_plate: '',
      model: '',
      photo: '',

      year: 0,

    },
  })

  const addCar = async (data: CreateCar) => {
    await CarsService.createCar({ requestBody: data })
  }

  const mutation = useMutation(addCar, {
    onSuccess: () => {
      showToast('Success!', 'Car created successfully.', 'success')
      reset()
      onClose()
    },
    onError: (err: ApiError) => {
      const errDetail = err.body.detail
      showToast('Something went wrong.', `${errDetail}`, 'error')
    },
    onSettled: () => {
      queryClient.invalidateQueries('cars')
    },
  })

  const onSubmit: SubmitHandler<CreateCar> = (data) => {
    mutation.mutate(data)
  }

  return (
    <>
      <Modal
        isOpen={isOpen}
        onClose={onClose}
        size={{ base: 'sm', md: 'md' }}
        isCentered
      >
        <ModalOverlay />
        <ModalContent as="form" onSubmit={handleSubmit(onSubmit)}>
          <ModalHeader>Add Car</ModalHeader>
          <ModalCloseButton />
          <ModalBody pb={6}>
            <FormControl isRequired isInvalid={!!errors.capacity}>
              <FormLabel htmlFor="capacity">Capacity</FormLabel>
              <Input
                id="capacity"
                {...register('capacity', {
                  required: 'capacity is required.',
                })}
                placeholder="capacity"
                type="text"
              />
              {errors.capacity && (
                <FormErrorMessage>{errors.capacity.message}</FormErrorMessage>
              )}
            </FormControl>

          </ModalBody>

          <ModalFooter gap={3}>
            <Button variant="primary" type="submit" isLoading={isSubmitting}>
              Save
            </Button>
            <Button onClick={onClose}>Cancel</Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </>
  )
}

export default AddCar
